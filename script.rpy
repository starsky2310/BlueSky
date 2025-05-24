init python:
    import math
define zzb = Character("造造") 
define fish = Character("梭特费斯")
default Money = 10 #金钱
default Sans = 100 #情绪
default Tired = 50 #疲劳度
default Study = 0 #学习
default Learn = 0  #累积学习值
default Days=300 #剩余天数
default Nowtime=0
default breakfast_flag=0
'''
init python:
    def time_pass(time):
        Nowtime+=time
        if Nowtime>=1440:
            Nowtime-=1440
            Days=Days-5
'''
label start:
    #call Hundred_Days
    call Zero #序章
    while(Days>195):
        call NormalDay
        $Days=Days-5
    "进入初见啥"
    call Meeting
    while(Days>100):
        call NormalDay
        $Days=Days-5
    call Hundred_Days
    while(Days>0):
        call NormalDay
    if Days==0: #正常结束，进入高考
        call The_End
    if Days==-1: #结局
        "你的人生就这样结束了"
        "你失去了高考的资格，人生的希望就这样破灭了"
        "你感到无比绝望，人生的希望就这样破灭了"
        "达成结局：被车创死"
        return
label Zero:  #序章
    scene 街头
    play music "audio/Shattered Paths.mp3" fadeout 5.0
    "盛夏，一轮旭日照在一座名叫冷锡的小城，夏日的蝉鸣与城市中的车水马龙混杂在一起，天朗气清，惠风和畅。"
    "铭在路上急匆匆的跑着，开学第一天，他可不想带上迟到的帽子。"
    with dissolve
    scene 校门
    "“冷锡市第一中学”，这几个大字刻在这扇并不算宏伟的校门上。"
    "“这是多少人，可望而不可及的学府。”"
    "“这是多少人，阶级跨越的殿堂。”"
    "“这是多少人的希望，与未来......”"
    with dissolve
    scene 教室
    "平平" "从今天开始，你们就正式算是高三了。"
    "平平" "希望你们好好读书，帮自己读。不是帮父母，帮老师。"
    "同学A" "说来说去就是这些 我耳朵都起茧子了……"
    with dissolve
    scene 晚自习教室
    "窗外的夜空里，闪烁着许多的星星"
    fish "我也能成为一颗星星吗……"
    #show text "当前时间：{Nowtime/60}：{Nowtime%60}，剩余天数：{Days}"
    return

label NormalDay: #正常的日常
    scene black
    #if Tired>=200 or Sans<=0:
    #    jump end0
    "距离高考还有：[Days]天"
    call wakeup
    call class_one
    call class_break
    call class_one
    call lunch
    call class_one
    call class_one
    call dinner
    call evening_class
    call evening_class
    call evening_class
    call Sleep
    return

label wakeup: #起床
    scene 卧室
    $Learn+=Study
    $Study=Study-math.sqrt(Study) #学的越多，忘的越快，所以不建议血太多（？
    $Flag1 = renpy.random.randint(0,int(Tired)) #随机一个0到疲劳值的数值
    $Flag2 = math.sqrt(renpy.random.randint(4,100))*0.1 #随机一个4到100的数值
    $Tired=Tired*(1-Flag2) #睡醒后自动降低一定的疲劳值（20%-100%）
    if Flag2<0.25:
        fish "昨晚上失眠了……"
    elif Flag2<0.5:
        fish "起来感觉迷迷糊糊的"
    elif Flag2<0.75:
        fish "昨晚感觉睡的还行"
    else:
        fish "神清气爽~"
    "叮铃铃叮铃铃~"
    if Tired>100: 
        fish "好困, 不想起床"
    menu:
        "关掉闹钟":
            pass
        "继续睡会":
            $Flag1+=10 #判定系数+10，可能迟到
            $Tired=Tired*0.9 #赖床，小幅度降低疲劳值 但是可能迟到
    if Flag1>100:
        fish "我去！睡过头了！"
        $Flag1= renpy.random.randint(1,10)
        menu:
            "急匆匆的赶往学校": #进行判断，10%概率被车创死，触发结局，10%几率触发时间："爱意"早餐（全游戏流程仅一次），
                if Flag1==10: #事件:被车创死
                    scene 街头
                    "你急忙赶往学校"
                    "忽然，一辆汽车从你身边飞驰而过"
                    if renpy.random.randint(1,Tired)>150:
                        "因为实在是太困了，你来不及反应，车子就撞上了你"
                        "你感到一阵剧痛，随即失去了意识"
                        jump end1
                    else:
                        "好在你反应及时，不然可就要Game Over咯"
                        "下次记得早点睡！"
                if Flag1==9: #事件：爱意早餐
                    if breakfast_flag!=1:
                        "妈妈" "诶诶，吃个早饭再走啊"
                        menu:
                            "再不出门就迟到了":
                                "妈妈" "那你怎么不早点起来，自己睡到这个点还怪我咯"
                                menu:
                                    "摔门而去":
                                        "你并没有理会母亲的责骂，直接摔门离开了家里"
                                        $Sans-=20
                                        "心情大幅降低"
                            "行吧，快点吃说不定还赶得上":
                                "为了不被骂，你经可能快速的吃完了早餐"
                                $Flag1-=renpy.random.randint(3,11) #迟到的概率增加到80%？
                        $breakfast_flag=1 #标志位置1
                    else:
                        "你急忙赶往学校，累的要死，可即便如此因为出门实在太晚，你还是迟到了"
                        $Tired+=10 
                        call late #迟到
                if Flag1<=4: #40%概率触发
                    "你急忙赶往学校，累的要死，可即便如此因为出门实在太晚，你还是迟到了"
                    $Tired+=10 
                    call late #迟到
                if 4<Flag1<9:
                    "你急匆匆赶往学校，赶在上课铃之前踩点进了教室"
                    $Tired+=10 
            "不急！": #100%触发迟到，但是不会增加疲劳（？
                "既然都要迟到了，那干脆慢点走咯~" 
                call late
                
    else:
        fish "（看了下表）时间还早，不急"
        fish "今天又是坐牢的一天呢"
    return
label late: #迟到
    "你来到教学楼下，发现年级主任正在抓迟到。"
    "尿建辉" "你看见你们老师看你的眼光了吗，嫌弃得你要死，你迟到扣分是要扣他工资的，你看他待会来不来领你吧"
    fish "……"
    $Sans=Sans-10
    return
label Sleep_in_Class:
    "平平" "你在干什么？"
    "平平" "睡觉？要睡回家去睡啊！来学校干什么？"
    fish "……"
    $Sans-=20
    return
label class_one: #上课
    scene 教室
    "上课时间到了~"
    if Tired>150:
        fish "好困~想睡觉~"
        menu:
            "听课":
                "你用手撑着头，努力保持清醒"
                fish "困死了，根本听不懂"
                $Sans-=5
                $Tired+=10
            "发呆":
                fish "非常无聊数学课 使我大脑死机"
                "你实在是太困了，忍不住睡着了"
                $Sans+=5
                $Tired-=10
                if renpy.random.randint(0,10)==10: #随机事件
                    call Sleep_in_Class
            "睡觉":
                fish "在CN Senior High Schoool上课没睡过觉的是这个👍"
                $Sans+=5
                $Tired-=15
                if renpy.random.randint(0,5)==5:
                    call Sleep_in_Class
    elif 50>Tired>100:
        "上课做点什么呢？"
        menu:
            "听课":
                "若存在过点(1,0)的直线与曲线y=x3和y=ax2……"
                fish "这点怎么就这么喜欢动呢？"
                $Sans+=5
                $Tired+=10
            "发呆":
                if renpy.random.randint(0,10)==10:
                    fish "不是这答案也太傻了吧，感觉不如……"
                    "你突然发现了一道题的巧妙解法，太酷啦~"
    return
label class_break:
    scene 走廊
    $Flag1 = renpy.random.randint(0,5) #随机一个0到5的数值
    if Flag1==5:
        fish "今天好像不用跑操，去哪呢？"
    else:
        scene 
        play music "audio/Running.mp3"
        fish "又要跑操了……"
        fish "这玩意除了让咱累的要死和让教室出现一股汗味"
        fish "还有其他用吗？"
        $Tired+=10
        $Sans-=5
        "跑操结束，还剩下一点时间"
        play music "audio/Shattered Paths.mp3" fadeout 5.0
    menu:
            "教室睡觉！" if Flag1==5:
                "对于大部分中学生而言，短短的20分钟他们也能做一个美好的梦"
                $Tired-=10
                $Sans+=5
            "在教室学习" if Flag1==5:
                "卷！"
                $Study+=1/(Tired+50) #学习效率根据当前疲劳度决定，疲劳度为0时增长2点学识，疲劳为100时增长0.33，200时增长0.25
                $Sans-=5
                $Tired+=15
            "小卖部":
                pass
            "去书店转转" if(150<Days<250):
                pass
#label BookStore:
label lunch:
label dinner:
label evening_class:
    scene 晚自习教室

label Sleep: #睡觉
    scene 卧室
    $time=0
    "到家咯~"
    while True:
        $time+=1
        if Tired>=200:
            "你已经有点困了，记得早点休息"
        if time>5:
            $Tired+=10 #超时惩罚
            "时候不早了，记得早点休息"
        menu:
            "看书":
                "真正的卷王当然要开夜班！"
                $Study+=1/(Tired+50) #学习效率根据当前疲劳度决定，疲劳度为0时增长2点学识，疲劳为100时增长0.33，200时增长0.25
                if Tired<50:
                    fish "状态良好~感觉还能再做三套卷子~"
                elif Tired>200:
                    fish "好困，学不进东西，要不还是早点睡吧..."
                else:
                    fish "奇变偶不变，后面一句啥来着？"
                $Sans-=5
                $Tired+=15
               
            "玩手机":
                "你回到家，打开手机，开始玩手机"
                "你玩得很开心，心情也变得愉快了起来"
                $Sans+=10
                $Tired+=10
            "睡觉":
                "进入梦乡"
                return
label Hundred_Days: #100天触发事件
    play music "audio/最后一道大题.mp3" #背景音乐
    "谱写……华章！"
    menu: 
        "谱写华章！":
            pass
        "不卸原神！":
            pass
        "……":
            pass
label Meeting:    #195天触发事件
    fish "(图片)"
    fish "也算是见证历史了"
    fish "冷一的状元楼终究要承受不住了"
    fish "听说墙壁，天花板都开裂了"
    zzb "我们那会就说是危楼了的"
    zzb "还不准喊楼"
    zzb "说怕塌了"
label The_End: #高考结束
label end0:
    scene 结局0
    ""
label end1:
    scene 结局1
    "达成结局1 被车创死"
    $renpy.quit()