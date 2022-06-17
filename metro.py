#!/usr/bin/python3


class Metro:
    stations = ["gummudipoondi", "kavarapet", "ponneri", "anuppambattu", "minjur"]
    #def card():


    def ticket(self):
        tickets1 = 100
        tickets2 = 100
        tickets3 = 100
        tickets4 = 100
        tickets5 = 100
        stations = ["gummudipoondi", "kavarapet", "ponneri", "anuppambattu", "minjur"]
        count1 = 99
        count2 = 99
        count3 = 99
        count4 = 99
        count5 = 99
        
        while True:
            destination = input("enter the destination  :   ")
            #print(stations.index(destination))
            if destination in stations:
                ticket_values = stations.index(destination) + 1
                if ticket_values == 1:
                    print(tickets1-count1,"1")
                    count1 =- 1
                    if count1 == 0:
                        print("tokens finished")
                        break
                    else:
                        continue
                
                elif ticket_values == 2:
                    print(tickets2, "2")
                    count2 =-1
                    if count2 == 0:
                        print("tokens finished")
                        break
                    else:
                        continue
                    

                elif ticket_values == 3:
                    print(tickets3, "3")
                    count3 =-1
                    if count3 == 0:
                        print("tokens finished")
                        break
                    else:
                        continue
                    

                elif ticket_values == 4:
                    print(tickets4, "4")
                    count4 =-1
                    if count4 == 0:
                        print("tokens finished")
                        break
                    else:
                        continue
                    

                elif ticket_values == 5:
                    print(tickets5 - count5, "5")
                    count5 =-1
                    if count5 == 0:
                        print("tokens finished")
                        break
                    else:
                        continue
                    
                else:
                    break

            else:
                print("enter correct destination")

obj = Metro()
#obj.card()
obj.ticket()
