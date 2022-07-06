import pygame
import sys
import time
pygame.init()
screen=pygame.display.set_mode((720,720))
w1=210
h1=80
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
font = pygame.font.Font('freesansbold.ttf', 32)
font4 = pygame.font.Font('freesansbold.ttf', 31)
font8 = pygame.font.Font('freesansbold.ttf', 17)
p=0

def home_button_v_1(x1,y1,button_text_1,coords_1,button_text_2,coords_2):
    if x1 <= pygame.mouse.get_pos()[0] <= x1+w1 and y1 <= pygame.mouse.get_pos()[1] <= y1+h1:
        pygame.draw.rect(screen,green,[x1,y1,w1,h1])
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y==1:
                    search()
                elif y==2:
                    sort()
                elif y==3:
                    make_graph()
                elif y==4:
                    show_full_default_data()
    else:
        pygame.draw.rect(screen,blue,[x1,y1,w1,h1])
    text_1 = font.render(button_text_1, True, green)
    text_2 = font.render(button_text_2, True, green)
    screen.blit(text_1, coords_1)
    screen.blit(text_2, coords_2)



def search_page_button_v_1(x1,y1,button_text_1,coords_1,button_text_2,coords_2,a):
    if x1 <= pygame.mouse.get_pos()[0] <= x1+w1 and y1 <= pygame.mouse.get_pos()[1] <= y1+h1:
        pygame.draw.rect(screen,green,[x1,y1,w1,h1])
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if a==1:
                    search_by_year()
                elif a==2:
                    search_by_area()
                elif a==3:
                    search_by_production()
                elif a==4:
                    search_by_visitation()
    else:
        pygame.draw.rect(screen,blue,[x1,y1,w1,h1])
    text_1 = font.render(button_text_1, True, green)
    text_2 = font.render(button_text_2, True, green)
    screen.blit(text_1, coords_1)
    screen.blit(text_2, coords_2)

def sort_page_button_v_1(x1,y1,button_text_1,coords_1,button_text_2,coords_2,a):
    if x1 <= pygame.mouse.get_pos()[0] <= x1+w1 and y1 <= pygame.mouse.get_pos()[1] <= y1+h1:
        pygame.draw.rect(screen,green,[x1,y1,w1,h1])
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if a==1:
                    sort_by_year()
                elif a==2:
                    sort_by_area()
                elif a==3:
                    sort_by_production()
                elif a==4:
                    sort_by_visitation()
    else:
        pygame.draw.rect(screen,blue,[x1,y1,w1,h1])
    text_1 = font.render(button_text_1, True, green)
    text_2 = font.render(button_text_2, True, green)
    screen.blit(text_1, coords_1)
    screen.blit(text_2, coords_2)



def button_v_2():
    pygame.draw.rect(screen,blue,[0,0,80,30])
    button_text_3 = "Back"
    text_3 = font.render(button_text_3, True, green)
    screen.blit(text_3, [2,2])


   
def sign(sign_text_1,sign_text_2):
    pygame.draw.rect(screen,blue,[110,20,500,100])
    sign_surface_1 = font4.render(sign_text_1, True, green)
    sign_surface_2 = font4.render(sign_text_2, True, green)
    screen.blit(sign_surface_1, (110,20))
    screen.blit(sign_surface_2, (110,50))



def search():
    screen.fill(black)
    x=0
    while x!=1:
        pygame.event.get()
        sign("What do you want to search by?", " ")
        a=1
        search_page_button_v_1(110,210,'Year',(110,210),'',(110,240),1)
        a=2
        search_page_button_v_1(400,210,'Woodland',(400,210),'Area',(400,240),2)
        a=3
        search_page_button_v_1(110,470,'Wood',(110,470),'Production',(110,500),3)
        a=4
        search_page_button_v_1(400,470,'Woodland',(400,470),'Visitation',(400,500),4)
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()



def search_by_year():
    screen.fill(black)
    x=0
    a=0
    digit_counter=0
    sby_text=["7","8","9","4","5","6","1","2","3","0"," "," "," "," ","Go"]
    x_coords=[200,250,300,200,250,300,200,250,300,200,200,250,300,350,250]
    y_coords=[200,200,200,250,250,250,300,300,300,350,100,100,100,100,350]
    input_list=[" "," "," "," "]
    while x!=1:
        pygame.event.get()
        w2=45
        h2=45
        for i in range(15):
            pygame.draw.rect(screen,blue,[x_coords[i],y_coords[i],w2,h2])
        for i in range(15):
            text_5 = font.render(sby_text[i], True, green)
            screen.blit(text_5, (x_coords[i],y_coords[i]))
            if x_coords[i] <= pygame.mouse.get_pos()[0] <= x_coords[i]+w2 and y_coords[i] <= pygame.mouse.get_pos()[1] <= y_coords[i]+h2:
                pygame.draw.rect(screen,green,[x_coords[i],y_coords[i],w2,h2])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if sby_text[i]!="Go":
                            sby_text[10+digit_counter]=sby_text[i]
                            digit_counter+=1
                        else:
                            for i in range(4):
                                input_list[i]=(sby_text[10+i])
                            x=1
                            a=1
                            screen.fill(black)                            
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
                    screen.fill(black)
        pygame.display.update()        
    if a==1:
        for i in range(len(raw_data)):
            current_year=raw_data[i]
            similarity_counter=0
            match_indicator=0
            for n in range(4):
                if current_year[n]==input_list[n]:
                    similarity_counter+=1
            if similarity_counter==4:
                print(raw_data[i])
                break
            if similarity_counter!=4:
                sign("year unavailable. To see years", "available see full default data")        
    screen.fill(black)
    x=0
    if a==1:
        while x!=1:
            pygame.event.get()
            pygame.draw.rect(screen,blue,[110,20,500,100])
            sign_surface_1 = font8.render("Year, Woodland area, Wood production, Woodland visitation", True, green)
            sign_surface_2 = font8.render(raw_data[i], True, green)
            screen.blit(sign_surface_1, (110,20))
            screen.blit(sign_surface_2, (110,50))
            button_v_2()
            if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
                pygame.draw.rect(screen,green,[0,0,80,30])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        x=1
            pygame.display.update()



def search_by_area():
    screen.fill(black)
    x=0
    a=0
    digit_counter=0
    sby_text=["7","8","9","4","5","6","1","2","3","0"," "," "," ","Go"]
    x_coords=[200,250,300,200,250,300,200,250,300,200,200,250,300,250]
    y_coords=[200,200,200,250,250,250,300,300,300,350,100,100,100,350]
    input_list=[" "," "," "]
    font8 = pygame.font.Font('freesansbold.ttf', 17)
    while x!=1:
        pygame.event.get()
        pygame.draw.rect(screen,blue,[200,45,500,50])
        text_9 = font8.render("Search by area % without decimal point.", True, green)
        screen.blit(text_9, (200,45))
        w2=45
        h2=45
        for i in range(14):
            pygame.draw.rect(screen,blue,[x_coords[i],y_coords[i],w2,h2])
        for i in range(14):
            text_5 = font.render(sby_text[i], True, green)
            screen.blit(text_5, (x_coords[i],y_coords[i]))
            if x_coords[i] <= pygame.mouse.get_pos()[0] <= x_coords[i]+w2 and y_coords[i] <= pygame.mouse.get_pos()[1] <= y_coords[i]+h2:
                pygame.draw.rect(screen,green,[x_coords[i],y_coords[i],w2,h2])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if sby_text[i]!="Go":
                            sby_text[10+digit_counter]=sby_text[i]
                            digit_counter+=1
                        else:
                            for i in range(3):
                                input_list[i]=(sby_text[10+i])
                            x=1
                            a=1
                            screen.fill(black)
                           
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
                    screen.fill(black)
        pygame.display.update()
       
    if a==1:
        for i in range(len(raw_data)):
            similarity_counter=0
            current_year=raw_data[i]
            for n in range(3):
                for b in range(len(current_year)):
                    if current_year[b]==".":
                        current_year=current_year.replace(".", "")
                        break
                if current_year[n+5]==input_list[n]:
                    similarity_counter+=1
            if similarity_counter==3:
                break            
        if similarity_counter!=3:
            sign("year unavailable. To see years", "available see full default data")        
    screen.fill(black)
    x=0
    j=0
    if a==1:
        while x!=1:
            pygame.event.get()
            pygame.draw.rect(screen,blue,[110,20,500,100])
            sign_surface_1 = font8.render("Year, Woodland area, Wood production, Woodland visitation", True, green)
            sign_surface_2 = font8.render(current_year, True, green)
            screen.blit(sign_surface_1, (110,20))
            screen.blit(sign_surface_2, (110,50))
            button_v_2()
            if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
                pygame.draw.rect(screen,green,[0,0,80,30])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        x=1
            pygame.display.update()


       
def search_by_production():
    screen.fill(black)
    x=0
    a=0
    digit_counter=0
    sby_text=["7","8","9","4","5","6","1","2","3","0"," "," "," "," "," ","Go"]
    x_coords=[200,250,300,200,250,300,200,250,300,200,200,250,300,350,400,250]
    y_coords=[200,200,200,250,250,250,300,300,300,350,100,100,100,100,100,350]
    input_list=[" "," "," "," "," "]
    while x!=1:
        pygame.event.get()
        w2=45
        h2=45
        for i in range(16):
            pygame.draw.rect(screen,blue,[x_coords[i],y_coords[i],w2,h2])
        for i in range(16):
            text_10 = font.render(sby_text[i], True, green)
            screen.blit(text_10, (x_coords[i],y_coords[i]))
            if x_coords[i] <= pygame.mouse.get_pos()[0] <= x_coords[i]+w2 and y_coords[i] <= pygame.mouse.get_pos()[1] <= y_coords[i]+h2:
                pygame.draw.rect(screen,green,[x_coords[i],y_coords[i],w2,h2])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if sby_text[i]!="Go":
                            sby_text[10+digit_counter]=sby_text[i]
                            digit_counter+=1
                        else:
                            for i in range(5):
                                input_list[i]=(sby_text[10+i])
                            x=1
                            a=1
                            screen.fill(black)                            
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
                    screen.fill(black)
        pygame.display.update()      
    if a==1:
        for i in range(len(raw_data)):
            current_year=raw_data[i]
            current_year_list=current_year.split(",")
            (",".join(input_list))
            similarity_counter=0
            match_indicator=0
            for n in range(len(current_year_list[2])):
                print("current_year_list: " + str(current_year_list))
                print("current_year_list[2][n]: " + str(current_year_list[2][n]))
                print("input_list[n]: " + str(input_list[n]))
                if current_year_list[2][n]==input_list[n]:
                    similarity_counter+=1
                print("similarity_counter: " + str(similarity_counter))
            if similarity_counter==5:
                print(raw_data[i])
                break
            if similarity_counter!=5:
                sign("year unavailable. To see years", "available see full default data")        
    screen.fill(black)
    x=0
    if a==1:
        while x!=1:
            pygame.event.get()
            pygame.draw.rect(screen,blue,[110,20,500,100])
            font8 = pygame.font.Font('freesansbold.ttf', 17)
            sign_surface_3 = font8.render("Year, Woodland area, Wood production, Woodland visitation", True, green)
            sign_surface_4 = font8.render(raw_data[i], True, green)
            screen.blit(sign_surface_3, (110,20))
            screen.blit(sign_surface_4, (110,50))
            button_v_2()
            if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
                pygame.draw.rect(screen,green,[0,0,80,30])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        x=1
            pygame.display.update()


       
def search_by_visitation():
    screen.fill(black)
    x=0
    a=0
    digit_counter=0
    sby_text=["7","8","9","4","5","6","1","2","3","0"," "," ","Go"]
    x_coords=[200,250,300,200,250,300,200,250,300,200,200,250,250]
    y_coords=[200,200,200,250,250,250,300,300,300,350,100,100,350]
    input_list=[" "," "]
    while x!=1:
        pygame.event.get()
        w2=45
        h2=45
        for i in range(13):
            pygame.draw.rect(screen,blue,[x_coords[i],y_coords[i],w2,h2])
        for i in range(13):
            text_10 = font.render(sby_text[i], True, green)
            screen.blit(text_10, (x_coords[i],y_coords[i]))
            if x_coords[i] <= pygame.mouse.get_pos()[0] <= x_coords[i]+w2 and y_coords[i] <= pygame.mouse.get_pos()[1] <= y_coords[i]+h2:
                pygame.draw.rect(screen,green,[x_coords[i],y_coords[i],w2,h2])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if sby_text[i]!="Go":
                            sby_text[10+digit_counter]=sby_text[i]
                            digit_counter+=1
                        else:
                            for i in range(2):
                                input_list[i]=(sby_text[10+i])
                            x=1
                            a=1
                            screen.fill(black)                            
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
                    screen.fill(black)
        pygame.display.update()      
    if a==1:
        for i in range(len(raw_data)):
            current_year=raw_data[i]
            current_year_list=current_year.split(",")
            (",".join(input_list))
            similarity_counter=0
            match_indicator=0
            for n in range(len(current_year_list[3])):
                print("current_year_list: " + str(current_year_list))
                print("current_year_list[3][n]: " + str(current_year_list[3][n]))
                print("input_list[n]: " + str(input_list[n]))
                if current_year_list[3][n]==input_list[n]:
                    similarity_counter+=1
                print("similarity_counter: " + str(similarity_counter))
            if similarity_counter==2:
                print(raw_data[i])
                break
            if similarity_counter!=2:
                sign("year unavailable. To see years", "available see full default data")        
    screen.fill(black)
    x=0
    if a==1:
        while x!=1:
            pygame.event.get()
            pygame.draw.rect(screen,blue,[110,20,500,100])
            font8 = pygame.font.Font('freesansbold.ttf', 17)
            sign_surface_3 = font8.render("Year, Woodland area, Wood production, Woodland visitation", True, green)
            sign_surface_4 = font8.render(raw_data[i], True, green)
            screen.blit(sign_surface_3, (110,20))
            screen.blit(sign_surface_4, (110,50))
            button_v_2()
            if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
                pygame.draw.rect(screen,green,[0,0,80,30])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        x=1
            pygame.display.update()


       
def sort():
    screen.fill(black)
    x=0
    while x!=1:
        pygame.event.get()
        sign("What do you want to sort by?", " ")
        a=1
        sort_page_button_v_1(110,210,'Year',(110,210),'',(110,240),1)
        a=2
        sort_page_button_v_1(400,210,'Woodland',(400,210),'Area',(400,240),2)
        a=3
        sort_page_button_v_1(110,470,'Wood',(110,470),'Production',(110,500),3)
        a=4
        sort_page_button_v_1(400,470,'Woodland',(400,470),'Visitation',(400,500),4)
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()


       
def sort_by_year():
    raw_data.reverse()
    screen.fill(black)
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(22):
        sorted_surface = font2.render(raw_data[i], True, green)
        screen.blit(sorted_surface, (1,int(i*24+165)))
    x=0
    while x!=1:
        pygame.event.get()
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()
def sort_by_area():
    screen.fill(black)
    element_holder=[]
    index_holder=[]
    reject_holder=[]
    sorted_data=[]
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(len(raw_data)):
        raw_data[i].split(",")
    for i in range(len(raw_data)):
        element_holder.append(raw_data[i][1])
    for i in range(len(raw_data)):
        if element_holder[i]=="p" or element_holder[i]=="*":
            reject_holder.append(element_holder[i])
            del element_holder[i]
    sorted_elements=sorted(element_holder)
    for i in range(len(sorted_elements)):
        for n in range(len(raw_data)):
            if sorted_elements[i]==raw_data[n][1]:
                sorted_data.append(raw_data[n])
    for i in range(len(reject_holder)):
        for n in range(len(raw_data)):
            if reject_holder[i]==raw_data[n][1]:
                sorted_data.append(raw_data[n])
    sorted_data_list=[]
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(15):
        print(raw_data[i])
        sorted_data_list.append(font2.render(raw_data[i], True, green))
        screen.blit(sorted_data_list[i], (1,int(i*24+165)))
                   
    x=0
    while x!=1:
        pygame.event.get()
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()

   
def sort_by_production():
    screen.fill(black)
    element_holder=[]
    index_holder=[]
    reject_holder=[]
    sorted_data=[]
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(len(raw_data)):
        raw_data[i]=raw_data[i].split(",")
    for i in range(len(raw_data)):
        element_holder.append(raw_data[i][2])
    n=0
    for i in range(len(element_holder)):
        if element_holder[n]=="p" or element_holder[n]=="*":
            reject_holder.append(element_holder[n])
            del element_holder[n]
            n-=1
        n+=1
    sorted_elements=sorted(element_holder)
    for i in range(len(sorted_elements)):
        for n in range(len(raw_data)):
            if sorted_elements[i]==raw_data[n][2]:
                sorted_data.append(raw_data[n])
    m=0
    for i in range(len(reject_holder)):
        if reject_holder[i]=="*":
            m+=1
    t=0
    for i in range(len(reject_holder)):
        while t<m:
            for n in range(len(raw_data)):
                if reject_holder[i]==raw_data[n][2]:
                    sorted_data.append(raw_data[n])
                    t+=1
    m=0
    for i in range(len(reject_holder)):
        if reject_holder[i]=="p":
            m+=1
    t=0
    for i in range(len(reject_holder)-m):
        while t<m:
            for n in range(len(raw_data)):
                if reject_holder[i+8]==raw_data[n][2]:
                    sorted_data.append(raw_data[n])
                    t+=1                    
    sorted_data_list=[]
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(22):
        joined_data=','.join(sorted_data[i])
        sorted_data_list.append(font2.render(joined_data, True, green))
        screen.blit(sorted_data_list[i], (1,int(i*24+165)))                  
    x=0
    while x!=1:
        pygame.event.get()
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()

def sort_by_visitation():
    screen.fill(black)
    element_holder=[]
    index_holder=[]
    reject_holder=[]
    sorted_data=[]
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(len(raw_data)):
        raw_data[i]=raw_data[i].split(",")
    for i in range(len(raw_data)):
        element_holder.append(raw_data[i][3])
    n=0
    for i in range(len(element_holder)):
        if element_holder[n]=="p" or element_holder[n]=="*":
            reject_holder.append(element_holder[n])
            del element_holder[n]
            n-=1
        n+=1
    sorted_elements=sorted(element_holder)
    for i in range(len(sorted_elements)):
        for n in range(len(raw_data)):
            if sorted_elements[i]==raw_data[n][3]:
                sorted_data.append(raw_data[n])
    m=0
    for i in range(len(reject_holder)):
        if reject_holder[i]=="*":
            m+=1
    t=0
    for i in range(len(reject_holder)):
        while t<m:
            for n in range(len(raw_data)):
                if reject_holder[i]==raw_data[n][3]:
                    sorted_data.append(raw_data[n])
                    t+=1
    m=0
    for i in range(len(reject_holder)):
        if reject_holder[i]=="p":
            m+=1
    t=0
    for i in range(len(reject_holder)-m):
        while t<m:
            for n in range(len(raw_data)):
                if reject_holder[i+8]==raw_data[n][3]:
                    sorted_data.append(raw_data[n])
                    t+=1                    
    sorted_data_list=[]
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(22):
        joined_data=','.join(sorted_data[i])
        sorted_data_list.append(font2.render(joined_data, True, green))
        screen.blit(sorted_data_list[i], (1,int(i*24+165)))                  
    x=0
    while x!=1:
        pygame.event.get()
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()
def make_graph():
    x=1
def make_mixed_graph():
    x=1
def show_full_default_data():
    screen.fill(black)
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    text_list=[]
    font3 = pygame.font.Font('freesansbold.ttf', 19)
    key_text=[]
    for i in range(22):
        text_list.append(font2.render(raw_data[i], True, green))
    for i in range(7):
        key_text.append(font3.render(data_desc_and_key[i], True, green))
    x=0
    while x!=1:
        pygame.event.get()
        for i in range(22):
            screen.blit(text_list[i], (1,int(i*24+165)))
        for i in range(7):
            screen.blit(key_text[i], (1,int(30+i*18)))
        button_v_2()
        if 0 <= pygame.mouse.get_pos()[0] <= 80 and 0 <= pygame.mouse.get_pos()[1] <= 30:
            pygame.draw.rect(screen,green,[0,0,80,30])
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    x=1
        pygame.display.update()

raw_data=[    
 "1905,4.7,*,*",
 "1924,5.0,*,*",
 "1947,5.9,*,*",
 "1965,7.4,*,*",
 "1980,9.0,*,*",
 "1995-1999(1997 used),11.3,*,*",
 "1998,12.0,*,*",
 "2011,*,10596,67",
 "2012,*,10628,*",
 "2013,*,11467,66",
 "2014,12.9,12063,*",
 "2015,13.0,11224,56",
 "2016,13.0,11341,*",
 "2017,13.1,11573,61",
 "2018,13.1,12184,*",
 "2019,13.1,10691,63",
 "2020,13.2,10880,*",
 "2021,13.3,*,69",
 "2022,p,p,p",
 "2023,p,p,p",
 "2024,p,p,p",
 "2025,p,p,p"]

data_desc_and_key=[
    "data displayed as follows:",
    "Year, Woodland Area (% area of UK)",
    "Wood Production (thousand green tonnes of roundwood)",
    "Woodland Visitation (% respondents visiting in 'last few years;",
    "Key:",
    "'*': no datum available from data set.",
    "'p': Value to be predicted by program via calculation upon user's request."]

def secondary_calculations():
    data_after_secondary_calcs=[]
    proportional_public_woodland_usage="*"
    proportional_commercial_woodland_usage="*"
    disruption_ratio="*"
    for i in range(len(raw_data)):
        primary_data=raw_data[i].split(",")
        if primary_data[3]!="*" and primary_data[3]!="p":
            if primary_data[1]!="*" and primary_data[1]!="p":
                proportional_public_woodland_usage=str(int(primary_data[3])/float(primary_data[1]))                
            if primary_data[2]!="*" and primary_data[2]!="p":
                disruption_ratio=str(int(primary_data[2])/int(primary_data[3]))
        if primary_data[2]!="*" and primary_data[2]!="p":
            if primary_data[1]!="*" and primary_data[1]!="p":
                proportional_commercial_woodland_usage=str(int(primary_data[2])/float(primary_data[1]))        
        primary_data.extend([proportional_public_woodland_usage,proportional_commercial_woodland_usage,disruption_ratio])
        data_after_secondary_calcs.append(primary_data)

secondary_calculations()                      
while True:
    pygame.event.get()
    screen.fill(black)
    sign("Forestry Statistics explorer","Select a button")
    y=1
    home_button_v_1(110,210,'Search',(110,210), ' ', (0,0))
    y=2
    home_button_v_1(400,210,'Sort',(400,210), ' ', (0,0))
    y=3
    home_button_v_1(110,470,'Make Graph',(110,470), ' ', (0,0))
    y=4
    home_button_v_1(400,470,'Show full',(400,470), 'default data', (400,500))
    pygame.display.update()

