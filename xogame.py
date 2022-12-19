def  xogame(message, xo):
    if xo[message.author][2]==True:
        x=int(message.content.split()[1])
        y=int(message.content.split()[2])
        if xo[message.author][1][x-1][y-1]=="#":
            xo[message.author][1][x-1][y-1]=xo[message.author][3]
            xo[xo[message.author][0]][1][x-1][y-1]=xo[message.author][3]
            res=""""""
            e=True
            f=True
            g=False
            for i in range (3):
                c=True
                d=True
                if xo[message.author][1][i][i]!=xo[message.author][1][0][0] or xo[message.author][1][i][i]=="#":
                    e=False
                if xo[message.author][1][i][2-i]!=xo[message.author][1][0][2] or xo[message.author][1][i][2-i]=="#":
                    f=False
                for j in range(3):
                    res+=xo[message.author][1][i][j]
                    res+=" "
                    if xo[message.author][1][i][j]!=xo[message.author][1][i][0] or xo[message.author][1][i][j]=="#":
                        c=False
                    if xo[message.author][1][j][i]!=xo[message.author][1][0][i] or xo[message.author][1][j][i]=="#":
                        d=False
                if c==True or d==True:
                    g=True
                res+="\n"
                    
                
                
            xo[message.author][4]+=1
            xo[xo[message.author][0]][4]+=1
            print(xo[message.author][4])
            xo[message.author][2]=False
            xo[xo[message.author][0]][2]=True
            if g==True or e==True or f==True:
                xo.pop(xo[message.author][0])
                xo.pop(message.author)
                res+= f"{message.author}"
                res+=" won"
            return res

        else:
            return "The place is already taken"
    else:
        return "It's  not your turn"

    