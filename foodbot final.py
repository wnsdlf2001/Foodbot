from tkinter import*
from tkinter import messagebox
import random #TKinter 와 random import


food = [["샌드위치", "떡만두국", "주먹밥", "비프스튜", "감자스프","토스트", "죽", "밥버거", "시리얼", "샐러드", "버섯스프", "콘스프", "체다치즈스프", "스크램블드에그", "요거트", "콩나물국밥", "뼈해장국", "순대국", "팬케이크", "굴국밥", "선지해장국", "맥앤치즈", "와플", "육개장", "리코타샐러드"],
["타코야끼", "크레페", "조각케익", "브라우니", "단팥빵", "크림빵", "완두앙금빵", "카스테라", "커스터드크림빵", "아메리카노", "라떼", "모카",
  "카라멜마끼아또", "핫초코","과일주스", "쿠키", "감자칩", "봉지과자", "아이스크림", "요거트", "츄러스", "마카롱" , "만두", "간식 5~10","빙수", "쉐이크", "와플", "컵케이크","스콘", "밀크티", "에끌레어", "화채"],
["라면", "김밥", "떡볶이", "순대", "김치볶음밥", "편의점도시락", "만두", "밥버거", "비빔국수",
 "쫄면", "케밥", "컵라면", "어묵꼬치", "짜장면",
  "짬뽕", "도너츠", "고로케","군만두", "물만두", "부리또", "핫도그","닭꼬치", "베이글", "컵밥",
 "우동", "햄버거", "마요덮밥", "오므라이스", "수제비", "비빔밥", "냉면", "돼지불고기", "카레", "제육볶음","순두부찌개", "김치찌개", "부대찌개",
  "된장찌개", "돈까스", "동태찌개", "갈치구이", "갈비탕", "칼국수", "짬뽕", "회덮밥", "굴국밥", "튀김덮밥", "라멘", "돈부리", "쌀국수", "김치찜", "갈비찜",
  "고등어조림", "곰탕", "삼계탕", "고추장찌개", "청국장",  "비빔냉면", "기스면", "볶음짬뽕", "짜장밥", "짬뽕밥", "새우볶음밥","오징어덮밥", "잡채밥", "콩국수",
  "왕만두", "메밀소바", "알밥","물회", "육개장", "제육덮밥", "규동", "사케동", "타코", "설렁탕", "돼지국밥", "매운탕", "황태국", "마라탕",
 "치킨", "토마토 파스타", "크림파스타", "오일 파스타", "초밥", "소불고기", "닭볶음탕", "닭갈비", "삼계탕", "쭈꾸미", "물회", "한정식", "퀘사디아",
  "샤브샤브", "조개구이", "떡갈비", "게장", "함박스테이크", "계란탕", "리조또", "필라프", "바비큐", "양고기", "오꼬노미야끼", "돼지불백", "콩불", "삼겹살", "육회",
  "곱창전골", "두부전골", "샤브샤브", "해물탕", "만두전골", "바비큐", "양고기", "연어","스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우", "라조육", "고추잡채", "팔보채", "유산술",
  "깐풍기", "장어구이", "랍스타","훠궈", "오리고기","스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우", "라조육", "고추잡채","팔보채", "유산술", "깐풍기", "장어구이", "랍스타", "훠궈", "오리고기", "보쌈", "대게", "양꼬치", "고기뷔페", "보쌈", "대게", "양꼬치", "고기뷔페", "홍어삼합"],
["라면", "김밥", "떡볶이", "순대", "김치볶음밥", "편의점도시락", "만두", "밥버거", "비빔국수", "쫄면", "케밥", "컵라면", "어묵꼬치", "짜장면",
  "짬뽕", "도너츠", "고로케","군만두", "물만두", "부리또", "핫도그","닭꼬치", "베이글", "컵밥","우동", "햄버거", "마요덮밥", "오므라이스", "수제비", "비빔밥", "냉면", "돼지불고기", "카레", "제육볶음","순두부찌개", "김치찌개", "부대찌개",
  "된장찌개", "돈까스", "동태찌개", "갈치구이", "갈비탕", "칼국수", "짬뽕", "회덮밥", "굴국밥", "튀김덮밥", "라멘", "돈부리", "쌀국수", "김치찜", "갈비찜",
  "고등어조림", "곰탕", "삼계탕", "고추장찌개", "청국장",  "비빔냉면", "기스면", "볶음짬뽕", "짜장밥", "짬뽕밥", "새우볶음밥","오징어덮밥", "잡채밥", "콩국수",
  "왕만두", "메밀소바", "알밥","물회", "육개장", "제육덮밥", "규동", "사케동", "타코", "설렁탕", "돼지국밥", "매운탕", "황태국", "마라탕", "치킨", "토마토 파스타", "크림파스타", "오일 파스타", "초밥", "소불고기", "닭볶음탕", "닭갈비", "삼계탕", "쭈꾸미", "물회", "한정식", "퀘사디아",
  "샤브샤브", "조개구이", "떡갈비", "게장", "함박스테이크", "계란탕", "리조또", "필라프", "바비큐", "양고기", "오꼬노미야끼", "돼지불백", "콩불", "삼겹살", "육회",
  "곱창전골", "두부전골", "샤브샤브", "해물탕", "만두전골", "바비큐", "양고기", "연어", "스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우", "라조육", "고추잡채", "팔보채", "유산술",
  "깐풍기", "장어구이", "랍스타","훠궈", "오리고기","스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우",
  "라조육", "고추잡채","팔보채", "유산술", "깐풍기", "장어구이", "랍스타", "훠궈", "오리고기", "보쌈", "대게", "양꼬치","고기뷔페", "보쌈", "대게", "양꼬치", "고기뷔페", "홍어삼합"],
["마른안주류", "콘치즈", "과자류", "닭강정", "고구마", "호떡", "붕어빵", "군밤", "스팸", "해쉬브라운", "카라아게", "핫바", "나초치즈","감자튀김", "돼지껍데기", "두부김치", "오코노미야키", "야끼소바", "치킨 너겟", "군만두", "닭강정", "매운탕", "화채", "계란찜",
  "골뱅이무침", "닭발", "치킨", "소시지야채볶음", "순대볶음", "육회", "양꼬치", "전", "양고기", "오뎅탕", "콩불","야식15","족발", "보쌈", "꼼장어", "야채곱창", "순대곱창"]]
#시간대별 음식데이터에 대한 리스트 작성
price= [["샌드위치", "떡만두국", "주먹밥", "비프스튜", "감자스프","토스트", "죽", "밥버거", "시리얼", "샐러드", "버섯스프", "콘스프", "체다치즈스프", "스크램블드에그", "요거트", "타코야끼", "크레페", "조각케익", "브라우니", "단팥빵", "크림빵", "완두앙금빵", "카스테라", "커스터드크림빵", "아메리카노", "라떼", "모카",
  "카라멜마끼아또", "핫초코","과일주스", "쿠키", "감자칩", "봉지과자", "아이스크림", "요거트", "츄러스", "마카롱" , "만두", "라면", "김밥", "떡볶이", "순대", "김치볶음밥", "편의점도시락", "만두", "밥버거", "비빔국수", "쫄면", "케밥", "컵라면", "어묵꼬치", "짜장면",
  "짬뽕", "도너츠", "고로케","군만두", "물만두", "부리또", "핫도그","닭꼬치", "베이글", "컵밥", "라면", "김밥", "떡볶이", "순대", "김치볶음밥", "편의점도시락", "만두", "밥버거", "비빔국수", "쫄면", "케밥", "컵라면", "어묵꼬치", "짜장면", "짬뽕", "도너츠", "고로케","군만두", "물만두", "부리또", "핫도그","닭꼬치", "베이글", "컵밥", "마른안주류", "콘치즈", "과자류", "닭강정", "고구마", "호떡", "붕어빵", "군밤", "스팸", "해쉬브라운", "카라아게", "핫바", "나초치즈"],["콩나물국밥", "뼈해장국", "순대국", "팬케이크", "굴국밥", "선지해장국", "맥앤치즈", "와플", "육개장","빙수", "쉐이크", "와플", "컵케이크","스콘", "밀크티", "에끌레어", "화채", "우동", "햄버거", "마요덮밥", "오므라이스", "수제비", "비빔밥", "냉면", "돼지불고기", "카레", "제육볶음","순두부찌개", "김치찌개", "부대찌개",
  "된장찌개", "돈까스", "동태찌개", "갈치구이", "갈비탕", "칼국수", "짬뽕", "회덮밥", "굴국밥", "튀김덮밥", "라멘", "돈부리", "쌀국수", "김치찜", "갈비찜",
  "고등어조림", "곰탕", "삼계탕", "고추장찌개", "청국장",  "비빔냉면", "기스면", "볶음짬뽕", "짜장밥", "짬뽕밥", "새우볶음밥","오징어덮밥", "잡채밥", "콩국수",
  "왕만두", "메밀소바", "알밥","물회", "육개장", "제육덮밥", "규동", "사케동", "타코", "설렁탕", "돼지국밥", "매운탕", "황태국", "마라탕", "치킨", "토마토 파스타", "크림파스타", "오일 파스타", "초밥", "소불고기", "닭볶음탕", "닭갈비", "삼계탕", "쭈꾸미", "물회", "한정식", "퀘사디아",
  "샤브샤브", "조개구이", "떡갈비", "게장", "함박스테이크", "계란탕", "리조또", "필라프", "바비큐", "양고기", "오꼬노미야끼", "돼지불백", "콩불", "삼겹살", "육회",
  "곱창전골", "두부전골", "샤브샤브", "해물탕", "만두전골", "바비큐", "양고기", "연어", "감자튀김", "돼지껍데기", "두부김치", "오코노미야키", "야끼소바", "치킨 너겟", "군만두", "닭강정", "매운탕", "화채", "계란찜"],["리코타샐러드","치킨", "토마토 파스타", "크림파스타", "오일 파스타", "초밥", "소불고기", "닭볶음탕", "닭갈비", "삼계탕", "쭈꾸미", "물회", "한정식", "퀘사디아",
  "샤브샤브", "조개구이", "떡갈비", "게장", "함박스테이크", "계란탕", "리조또", "필라프", "바비큐", "양고기", "오꼬노미야끼", "돼지불백", "콩불", "삼겹살", "육회",
  "곱창전골", "두부전골", "샤브샤브", "해물탕", "만두전골", "바비큐", "양고기", "연어", "치킨", "토마토 파스타", "크림파스타", "오일 파스타", "초밥", "소불고기", "닭볶음탕", "닭갈비", "삼계탕", "쭈꾸미", "물회", "한정식", "퀘사디아",
  "샤브샤브", "조개구이", "떡갈비", "게장", "함박스테이크", "계란탕", "리조또", "필라프", "바비큐", "양고기", "오꼬노미야끼", "돼지불백", "콩불", "삼겹살", "육회",
  "곱창전골", "두부전골", "샤브샤브", "해물탕", "만두전골", "바비큐", "양고기", "연어", "골뱅이무침", "닭발", "치킨", "소시지야채볶음", "순대볶음", "육회", "양꼬치", "전", "양고기", "오뎅탕", "콩불"],["스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우", "라조육", "고추잡채", "팔보채", "유산술",
  "깐풍기", "장어구이", "랍스타","훠궈", "오리고기","스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우",
  "라조육", "고추잡채","팔보채", "유산술", "깐풍기", "장어구이", "랍스타", "훠궈", "오리고기", "보쌈", "대게", "양꼬치","고기뷔페", "보쌈", "대게", "양꼬치", "고기뷔페", "홍어삼합", "스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우", "라조육", "고추잡채", "팔보채", "유산술",
  "깐풍기", "장어구이", "랍스타","훠궈", "오리고기","스테이크", "호텔식뷔페", "족발", "갈비찜", "피자", "회", "한정식", "감자탕", "탕수육", "마파두부", "깐쇼새우",
  "라조육", "고추잡채","팔보채", "유산술", "깐풍기", "장어구이", "랍스타", "훠궈", "오리고기", "보쌈", "대게", "양꼬치","고기뷔페", "보쌈", "대게", "양꼬치", "고기뷔페", "홍어삼합", "족발", "보쌈", "꼼장어", "야채곱창", "순대곱창"]]
#가격대별 음식데이터에 대한 리스트 작성
alergie = [["감자스프", "시리얼", "버섯스프", "콘스프", "체다치즈스프", "요거트", "라떼", "모카", "카라멜마끼아또", "핫초코", "아이스크림", "요거트", "빙수", "쉐이크", "밀크티"],
           ["스크램블드에그", "계란탕", "계란찜"],
           ["콩국수", "두부전골"],
           ["닭꼬치","삼계탕","닭도리탕","치킨", "닭갈비","닭강정","닭발","깐풍기"],
           ["감자탕", "돼지불백", "삼겹살", "콩나물불고기", "돼지국밥", "제육덮밥", "순대국", "족발","보쌈", "스팸", "돼지껍데기"],
           ["소불고기", "갈비탕," "스테이크", "갈비찜", "규동", "육회"],
           ["어묵꼬치", "매운탕", "오뎅탕", "사케동", "연어", "갈치구이", "고등어조림", "황태국", "꼼장어", "장어구이", "동태찌개"]]
#알러지에 대한 음식데이터 리스트 작성

checkvar_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def lastpage():#마지막으로 추첨을 통해 결과창를 보여주는 함수
    top1 = Toplevel()

    top1.title("추천음식입니다")
    top1.geometry("400x400")
    fooda = choose()#choose 함수의 리턴값을 불러와 변수에 저장한다
    
    C = Canvas(top1, bg="gray", height=400, width=400)
    filename2 = PhotoImage(file = "images/%s.png"%fooda)
    background_label1 = Label(top1, image=filename2)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
   
    

    
    
    frame=Frame(top1)
    frame.pack()

    bottomframe = Frame(top1)
    bottomframe.pack(side=BOTTOM)

    morebutton = Button(bottomframe, text="음..한번더!", bg='white', fg='red', width=15, height=3,command = lastpage)
    morebutton.pack(side='left',padx=30,pady=10)#lastpage함수가 한번 더 실행되게 한다
    
    morebutton2 = Button(bottomframe, text="다시 선택지로", bg='white', fg='red', width=15, height=3,command = menu)
    morebutton2.pack(side='left',padx=30,pady=10)#menu 함수로 돌아가 다시 선택하도록 한다.

   
    
    label1=Label(top1, text="%s!"%fooda,fg='sienna4', font=("바탕체",20),bg='systemwindow')

    label1.pack()
    C.pack()
    
    top1.mainloop()
    
def copyr():#저작권 부분을 창으로 띄워주는 함수
    top=Tk()
    label10=Label(top, text="Copyright\n",fg='sienna4', font=("바탕체",10),bg='snow')
    label11=Label(top, text="2011301742 윤준일",fg='sienna4', font=("바탕체",10),bg='snow')
    label12=Label(top, text="2012311567 장성훈",fg='sienna4', font=("바탕체",10),bg='snow')
    label13=Label(top, text="2014312463 이은지",fg='sienna4', font=("바탕체",10),bg='snow')
    label14=Label(top, text="2015310826 박정현",fg='sienna4', font=("바탕체",10),bg='snow')


    label10.pack()
    label11.pack()
    label12.pack()
    label13.pack()
    label14.pack()



def choose():#선택지에 기반하여 음식을 골라주는 함수
    final1 = []
    final2 = []
    final3 =[]
    whole1=[]
    whole2=[]
    whole3=[]
    if int(checkvar_list[0]) == 1 :#체크 유무를 1과 0으로 판단하여 1이면 리스트에 넣어줌
        rand = random.randint(0,len(food[0]))
        final1 += food[0]
    if int(checkvar_list[1]) == 1 :
        rand = random.randint(0,len(food[1]))
        final1 += food[1]
    if int(checkvar_list[2]) == 1 :
        rand = random.randint(0,len(food[2]))
        final1 += food[2]
    if int(checkvar_list[3]) == 1 :
        rand = random.randint(0,len(food[3]))
        final1 += food[3]
    if int(checkvar_list[4]) == 1 :
        rand = random.randint(0,len(food[4]))
        final1 += food[4]
    if int(checkvar_list[5]) == 1 :
        rand = random.randint(0,len(food[0]+food[1]+food[2]+food[3]+food[4]))
        whole1 = food[0]+food[1]+food[2]+food[3]+food[4]
        final1 += whole1 
    if int(checkvar_list[6]) == 1 :
        rand = random.randint(0,len(price[0]))
        final2 += price[0]
    if int(checkvar_list[7]) == 1 :
        rand = random.randint(0,len(price[1]))
        final2 += price[1]
    if int(checkvar_list[8]) == 1 :
        rand = random.randint(0,len(price[2]))
        final2 += price[2]
    if int(checkvar_list[9]) == 1 :
        rand = random.randint(0,len(price[3]))
        final2 += price[3]
    if int(checkvar_list[10]) == 1 :
        rand = random.randint(0,len(price[0]+price[1]+price[2]+price[3]))
        whole2 = price[0]+price[1]+price[2]+price[3]
        final2 += whole2
    if int(checkvar_list[11]) == 1 :
        rand = random.randint(0,len(alergie[0]))
        final3 += alergie[0]
    if int(checkvar_list[12]) == 1 :
        rand = random.randint(0,len(alergie[1]))
        final3 += alergie[1]
    if int(checkvar_list[13]) == 1 :
        rand = random.randint(0,len(alergie[2]))
        final3 += alergie[2]
    if int(checkvar_list[14]) == 1 :
        rand = random.randint(0,len(alergie[3]))
        final3 += alergie[3]
    if int(checkvar_list[15]) == 1 :
        rand = random.randint(0,len(alergie[4]))
        final3 += alergie[4]
    if int(checkvar_list[16]) == 1 :
        rand = random.randint(0,len(alergie[5]))
        final3 += alergie[5]
    if int(checkvar_list[17]) == 1 :
        rand = random.randint(0,len(alergie[6]))
        final3 += alergie[6]
    if int(checkvar_list[18]) == 1 :
        rand = random.randint(0,len(alergie[0] +alergie[1]+alergie[2]+alergie[3] +alergie[4]+alergie[5]+alergie[6]))
        whole3 = alergie[0] +alergie[1]+alergie[2]+alergie[3] +alergie[4]+alergie[5]+alergie[6]
        final3 += whole3
    
        
    final = set(final1).intersection(set(final2))#시간대와 가격별 음식데이터의 교집합을 통해 추천해줌
    if list(final) ==[]:#교집합이 없다면(음식이 없다면)
        return "카테고리에 음식이 없어요"
    else:#교집합이 있다면(음식이 있다면)
        final = list(final - set(final3))
        randomnum = random.randrange(0, len(final))
        return final[randomnum]


    
    
def setting_checkvar1():#menu 함수의 체크버튼을 1로 활성화시켜주는 함수들
    global checkvar_list
    checkvar_list[0] = 1
    
def setting_checkvar2():
    global checkvar_list
    checkvar_list[1] = 1
    
def setting_checkvar3():
    global checkvar_list
    checkvar_list[2] = 1
    
def setting_checkvar4():
    global checkvar_list
    checkvar_list[3] = 1
    
def setting_checkvar5():
    global checkvar_list
    checkvar_list[4] = 1
    
def setting_checkvar6():
    global checkvar_list
    checkvar_list[5] = 1
    
def setting_checkvar7():
    global checkvar_list
    checkvar_list[6] = 1
    
def setting_checkvar8():
    global checkvar_list
    checkvar_list[7] = 1
    
def setting_checkvar9():
    global checkvar_list
    checkvar_list[8] = 1
    
def setting_checkvar10():
    global checkvar_list
    checkvar_list[9] = 1
    
def setting_checkvar11():
    global checkvar_list
    checkvar_list[10] = 1
    
def setting_checkvar12():
    global checkvar_list
    checkvar_list[11] = 1
    
def setting_checkvar13():
    global checkvar_list
    checkvar_list[12] = 1
    
def setting_checkvar14():
    global checkvar_list
    checkvar_list[13] = 1

    
def setting_checkvar15():
    global checkvar_list
    checkvar_list[14] = 1
    
def setting_checkvar16():
    global checkvar_list
    checkvar_list[15] = 1
    
def setting_checkvar17():
    global checkvar_list
    checkvar_list[16] = 1
    
def setting_checkvar18():
    global checkvar_list
    checkvar_list[17] = 1
                              
def setting_checkvar19():
    global checkvar_list
    checkvar_list[18] = 1


def setting_initialize():#초기화를 실행했을 때 체크 현황과 리스트를 전부 0으로 바꿔주는 함수
    global checkvar_list
    checkvar_list = [0] * 19
    final1 = []
    final2 = []
    final3 =[]
    whole1=[]
    whole2=[]
    whole3=[]
    
def menu():#선택메뉴를 출력해주는 함수
   
    app=Tk()

    app.title("오늘 뭐먹지?")
    app.geometry("500x400")
    app.resizable(width = FALSE, height = FALSE)#버튼 정렬이 안되어 사이즈를 고정함

    
    checkvar1 = IntVar()
    checkvar2 = IntVar()
    checkvar3 = IntVar()
    checkvar4 = IntVar()
    checkvar5 = IntVar()
    checkvar6 = IntVar()
    checkvar7 = IntVar()
    checkvar8 = IntVar()
    checkvar9 = IntVar()
    checkvar10 = IntVar()
    checkvar11 = IntVar()
    checkvar12 = IntVar()
    checkvar13 = IntVar()
    checkvar14 = IntVar()
    checkvar15 = IntVar()
    checkvar16 = IntVar()
    checkvar17 = IntVar()
    checkvar18 = IntVar()
    checkvar19 =IntVar()


    i=Label(app,text="시간대", height=2, width=5)#선택지에 나타나있는 버튼들
    i.pack()
    i.place_configure(x=20,y=30)
    c1=Checkbutton(app, text="아침", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=5, command=setting_checkvar1)
    c1.pack()
    c1.place_configure(x=60,y=30)
    c2=Checkbutton(app, text="간식", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=5, command=setting_checkvar2)
    c2.pack()
    c2.place_configure(x=120,y=30)
    c3=Checkbutton(app, text="점심", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=5, command=setting_checkvar3)
    c3.pack()
    c3.place_configure(x=180,y=30)
    c4=Checkbutton(app, text="저녁", variable=checkvar4, onvalue=1, offvalue=0, height=2, width=5, command=setting_checkvar4)
    c4.pack()
    c4.place_configure(x=240,y=30)
    c5=Checkbutton(app, text="야식/안주", variable=checkvar5, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar5)
    c5.pack()
    c5.place_configure(x=300,y=30)
    c20 = Checkbutton(app, text ="상관없음", variable=checkvar6, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar6)
    c20.pack()
    c20.place_configure(x=390,y=30)
    c6=Label(app, text="가격대", height=2, width=5)
    c6.pack()
    c6.place_configure(x=20,y=100)
    c7=Checkbutton(app, text="~5천원", variable=checkvar7, onvalue=1, offvalue=0, height=2, width=5, command=setting_checkvar7)
    c7.pack()
    c7.place_configure(x=70,y=100)
    c8=Checkbutton(app, text="5천원~만원", variable=checkvar8, onvalue=1, offvalue=0, height=2, width=10, command=setting_checkvar8)
    c8.pack()
    c8.place_configure(x=130,y=100)
    c9=Checkbutton(app, text="만원~만5천원", variable=checkvar9, onvalue=1, offvalue=0, height=2, width=10, command=setting_checkvar9)
    c9.pack()
    c9.place_configure(x=230,y=100)
    c10=Checkbutton(app, text="만5천원~", variable=checkvar10, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar10)
    c10.pack()
    c10.place_configure(x=330,y=100)
    c21 = Checkbutton(app, text ="상관없음", variable=checkvar11, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar11)
    c21.pack()
    c21.place_configure(x=410,y=100)
    
    c11=Label(app, text="알러지", height=2, width=7)
    c11.pack()
    c11.place_configure(x=15,y=170)
    c12=Checkbutton(app, text="우유", variable=checkvar12, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar12)
    c12.pack()
    c12.place_configure(x=60,y=170)
    c13=Checkbutton(app, text="달걀", variable=checkvar13, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar13)
    c13.pack()
    c13.place_configure(x=130,y=170)
    c14=Checkbutton(app, text="콩", variable=checkvar14, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar14)
    c14.pack()
    c14.place_configure(x=190,y=170)
    c15=Checkbutton(app, text="닭", variable=checkvar15, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar15)
    c15.pack()
    c15.place_configure(x=250,y=170)
    c16=Checkbutton(app, text="돼지", variable=checkvar16, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar16)
    c16.pack()
    c16.place_configure(x=310,y=170)
    c17=Checkbutton(app, text="소", variable=checkvar17, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar17)
    c17.pack()
    c17.place_configure(x=370,y=170)
    c18=Checkbutton(app, text="생선", variable=checkvar18, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar18)
    c18.pack()
    c18.place_configure(x=430,y=170)
    c19=Checkbutton(app, text="상관없음", variable=checkvar19, onvalue=1, offvalue=0, height=2, width=7, command=setting_checkvar19)
    c19.pack()
    c19.place_configure(x=60,y=200)
    initialize = Button(app, text='초기화', command=setting_initialize)
    initialize.pack()
    initialize.place_configure(x=100, y=330)
    #초기화 버튼 : 체크를 잘못했거나 다시 체크하고싶을때 사용한다. 
    info=Label(app, text ="중복 선택 가능!", height =2, width =15)
    info.pack()
    info.place_configure(x=40, y=280)
    info=Label(app, text ="초기화 방법 : 1. 체크를 전부 푼다  2. 초기화를 누른 뒤 다시 체크한다", height =2, width =60)
    info.pack()
    info.place_configure(x=30, y=250)

    #체크현황을 바탕으로하여 lastpage로 추첨을 해줄수 있도록 연결해준다.
    d=Button(app, text ="추천음식 보러가기", width = 20, command = lastpage)
    d.pack(side ='bottom', padx = 5, pady = 20)


    app.mainloop()


#메인 함수 부분
top = Tk()



top.title("오늘 뭐 먹지?")
top.geometry("400x480")

C = Canvas(top, bg="blue", height=400, width=400)
filename = PhotoImage(file = "question.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


frame=Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack(side=BOTTOM)

startbutton = Button(bottomframe, text="시작하기",bg="dim gray",fg='white', width=15, height=3, command = menu)
startbutton.pack(side=LEFT, pady=10)#시작하여 menu 함수로 넘어가는 버튼


copyrightb = Button(bottomframe, text="COPYRIGHT", bg="dim gray", fg="white", width=15, height= 3, command = copyr)
copyrightb.pack(side=LEFT, padx=10, pady=10)#copyright를 보여주는 버튼


label1=Label(top, text="음식을 선택하기 힘든 여러분들을 위한",fg='sienna4', font="바탕체 15 bold")



label1.pack()


top.mainloop()
