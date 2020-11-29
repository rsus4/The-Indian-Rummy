# Name:Rishit Gupta
# Roll No:2019091
# Group1



import sys
import pygame
from pygame.locals import *
from random import randint
import pygame.mixer 
from pygame.locals import *
pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)


deck=[]
new_count=0

boolean=True
count=1
music_counter=1
selected_card=[]
#cardblind=card2
boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
#partial_deck=[]
BlUE=(0,0,255)
NEON=(57,255,20)
player1_cards=[]
discarded_cards=[]
player2_cards=[]

#pygame.mixer.music.load('yiruma.mp3')
#pygame.mixer.music.play(-1)
#sound=pygame.mixer.Sound('river_flows.mp3')
#sound.play()
#sound=pygame.mixer.Sound('river.m4p')
#sound.play()
Value=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
Suit=["S","C","D","H"]

def create_deck():
	for suit in Suit:
		for value in Value:
			deck.append(str(value)+suit)
	return deck

def draw_card(Deck):
	random_card=randint(0,len(Deck)-1)
	return Deck.pop(random_card)

def deal_war():
	while (len(new_deck)>26):
		player1_cards.append(draw_card(new_deck))
		player2_cards.append(draw_card(new_deck))

def swap_cards():
	CArd1=pygame.image.load("Cards/"+str(selected_card[0])+".png")
	CArd2=pygame.image.load("Cards/"+str(selected_card[1])+".png")

	CArd1=pygame.transform.scale(CArd1,(95,120))
	CArd2=pygame.transform.scale(CArd2,(95,120))

	temp=player1_cards[player1_cards.index(selected_card[1])]
	player1_cards[player1_cards.index(selected_card[1])]=player1_cards[player1_cards.index(selected_card[0])]
	player1_cards[player1_cards.index(selected_card[0])]=temp
	count=1
	pygame.display.flip()

"""def player1_turn():
	print(1)
	#if player1 selects open_card
	if event.type==MOUSEBUTTONDOWN:
		mx,my=pygame.mouse.get_pos()
		if 51<mx<1343 and  400<my<520:
			if event.type==MOUSEBUTTONDOWN:
				mx,my=pygame.mouse.get_pos()
				if 700<mx<800 and 253<my<370:
					if event.type==MOUSEBUTTONDOWN:
						mx,my=pygame.mouse.get_pos()
						if 76<mx<245 and 185<my<230:
							print("Player2's turn" )
							return """

"""def player1_turn():
	print(1)
	#if player1 selects open_card
	if event.type!=MOUSEBUTTONDOWN:
		mx,my=pygame.mouse.get_pos()
		if 51<mx<1343 and  400<my<520:
			if event.type==MOUSEBUTTONDOWN:
				mx,my=pygame.mouse.get_pos()
				if 700<mx<800 and 253<my<370:
					if event.type==MOUSEBUTTONDOWN:
						mx,my=pygame.mouse.get_pos()
						if 76<mx<245 and 185<my<230:
							print("Player2's turn" )
							return """
def player1_turn():
	if move_count!=new_count:
		print("Change Turns")
		player2_turn(blind_card)

"""def player2_turn(blind_card):
	player2_number=randint(0,len(player2_cards)-1)
	#swap_cards_pick(player2_cards[player2_number],)
	player2card=pygame.image.load("Cards/"+str(player2_cards[player2_number])+".png")
	player2card=pygame.transform.scale(player2card,(95,120))
	temp=player2_cards[player2_number]
	player2_cards[player2_number]=blind_card
	blind_card=temp
	pygame.display.flip()"""


def player2_turn(blind_card):
	global card2
	player2_number=randint(0,len(player2_cards)-1)
	print(player2_cards[player2_number])
	#swap_cards_pick(player2_cards[player2_number],)
	player2card=pygame.image.load("Cards/"+str(player2_cards[player2_number])+".png")
	player2card=pygame.transform.scale(player2card,(95,120))
	temp4=player2_cards[player2_number]
	player2_cards[player2_number]=blind_card
	blind_card=temp4
	print(blind_card)

	card2=pygame.image.load("Cards/"+str(blind_card)+".png")
	card2=pygame.transform.scale(card2,(95,120))
	print("f")
	#screen.blit(card2,(700,250))
	"""for event in pygame.event.get():
		if event.type==MOUSEBUTTONDOWN :
			print(1)
			screen.blit(card2,(700,250))"""
	pygame.display.flip()

#def player_2swap():



def swap_cards_pick(card70s,card71d):
	CArd1=pygame.image.load("Cards/"+str(card70s)+".png")
	CArd2=pygame.image.load("Cards/"+str(card71d)+".png")

	CArd1=pygame.transform.scale(CArd1,(95,120))
	CArd2=pygame.transform.scale(CArd2,(95,120))
	#blind_card=card70
	#cardblind=pygame.image.load("Cards/"+str(blind_card)+".png")
	#cardblind=pygame.transform.scale(cardblind,(95,120))

	temp2=card71d
	card2=card70s
	discarded_cards=[]
	selected_card=[]
	player1_cards[player1_cards.index(card70s)]=temp2

	"""open_card=draw_card(stock_pile)
	card2=pygame.image.load("Cards/"+str(open_card)+".png")
	card2=pygame.transform.scale(card2,(95,120))"""

	"""temp1=discarded_cards[0]
	discarded_cards=[]
	player1_cards[player1_cards.index(selected_card[0])]=temp1"""
	"""temp=player1_cards[pla]
	player1_cards[player1_cards.index(selected_card[1])]=player1_cards[player1_cards.index(selected_card[0])]
	player1_cards[player1_cards.index(selected_card[0])]=temp"""
	
	pygame.display.flip()

create_deck()
#print(deck)
new_deck=list(deck)
#print(len(new_deck))
deal_war()
stock_pile=new_deck
pygame.init()
size=width,height=1366,760
screen=pygame.display.set_mode(size)
bg2=pygame.image.load("bg2.png")
bg2=pygame.transform.scale(bg2,size)
screen.blit(bg2,(0,0))
submit=pygame.image.load("submit.png")
submit=pygame.transform.scale(submit,(100,100))
win=pygame.image.load("win.png")
win=pygame.transform.scale(win,(100,100))
"""bg3=pygame.image.load("bg3.png")
bg3=pygame.transform.scale(bg3,size)"""
bg10=pygame.image.load("bg10.png")
bg10=pygame.transform.scale(bg10,size)
#card=pygame.image.load("Cards/2H.png")
#card=pygame.transform.scale(card,(100,150))

stock_card=pygame.image.load("Cards/blue_back.png")
stock_card=pygame.transform.scale(stock_card,(95,120))

#screen.blit(card,(0,0))
open_card=draw_card(stock_pile)
card2=pygame.image.load("Cards/"+str(open_card)+".png")
card2=pygame.transform.scale(card2,(95,120))
#cardblind=card2
joker_card=draw_card(stock_pile)
card69=pygame.image.load("Cards/"+str(joker_card)+".png")
card69=pygame.transform.scale(card69,(95,120))
pygame.display.flip()
pygame.mixer.music.load('yiruma.mp3')
pygame.mixer.music.play(-1)
blind_card=open_card
done=False





#mx,my=pygame.mouse.get_pos()
#print(mx)
while not done:
	mx,my=pygame.mouse.get_pos()
	new_count=0
	move_count=new_count
	#print(mx)
	"""if music_counter==1:
		pygame.mixer.music.load('yiruma.mp3')
		pygame.mixer.music.play(-1)
	music_counter+=1"""

	#print(my)
	screen.blit(bg10,(0,0))
	screen.blit(stock_card,(600,250))
	screen.blit(card2,(700,250))
	screen.blit(card69,(1136,240))
	screen.blit(submit,(636,575))
	for cards in player1_cards:
		card=pygame.image.load("Cards/"+str(cards)+".png")
		card=pygame.transform.scale(card,(95,120))
		screen.blit(card,(50+player1_cards.index(cards)*100,400))


	for event in pygame.event.get():
		if (event.type==pygame.QUIT) :
			sys.exit()
		elif event.type==KEYDOWN and event.key==K_ESCAPE:
			sys.exit()
		elif event.type==MOUSEBUTTONDOWN:
			#screen.blit(card2,(200,100))
			#pygame.display.flip()
			mx,my=pygame.mouse.get_pos()
			if 51<mx<144 and 400<my<520 and count<3:
				if boolean_dict["c1"]==False:
					boolean_dict["c1"]=True
				else:
					boolean_dict["c1"]=False
				if boolean_dict["c1"]==True:
					pygame.draw.circle(screen,NEON,(95,540),10)
					count+=1
					print(count)
					selected_card.append(player1_cards[0])
					print(selected_card)
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						print(player1_cards)
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[0])
					count-=1
			elif 151<mx<244 and 400<my<520 and count<3:
				if boolean_dict["c2"]==False:
					boolean_dict["c2"]=True
				else:
					boolean_dict["c2"]=False
				if boolean_dict["c2"]==True:
					pygame.draw.circle(screen,NEON,(195,540),10)
					count+=1
					print(count)
					selected_card.append(player1_cards[1])
					print(selected_card)
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						print(player1_cards)
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[1])
					count-=1
			
			elif 250<mx<344 and 400<my<520 and count<3:
				if boolean_dict["c3"]==False:
					boolean_dict["c3"]=True
				else:
					boolean_dict["c3"]=False
				if boolean_dict["c3"]==True:
					pygame.draw.circle(screen,NEON,(295,540),10)
					count+=1
					selected_card.append(player1_cards[2])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[2])
					count-=1
			elif 351<mx<444 and 400<my<520 and count<3:
				if boolean_dict["c4"]==False:
					boolean_dict["c4"]=True
				else:
					boolean_dict["c4"]=False
				if boolean_dict["c4"]==True:
					pygame.draw.circle(screen,NEON,(395,540),10)
					count+=1
					print(count)
					selected_card.append(player1_cards[3])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[3])
					count-=1
					print(count)
			elif 451<mx<544 and 400<my<520 and count<3:
				if boolean_dict["c5"]==False:
					boolean_dict["c5"]=True
				else:
					boolean_dict["c5"]=False
				if boolean_dict["c5"]==True:
					pygame.draw.circle(screen,NEON,(495,540),10)
					count+=1
					print(count)
					selected_card.append(player1_cards[4])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[4])
					count-=1
					print(count)
			elif 551<mx<644 and 400<my<520 and count<3:
				if boolean_dict["c6"]==False:
					boolean_dict["c6"]=True
				else:
					boolean_dict["c6"]=False
				if boolean_dict["c6"]==True:
					pygame.draw.circle(screen,NEON,(595,540),10)
					count+=1
					selected_card.append(player1_cards[5])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[5])
					count-=1
			elif 651<mx<744 and 400<my<520 and count<3:
				if boolean_dict["c7"]==False:
					boolean_dict["c7"]=True
				elif boolean_dict["c7"]==True:
					boolean_dict["c7"]=False
				if boolean_dict["c7"]==True:
					selected_card.append(player1_cards[6])
					pygame.draw.circle(screen,NEON,(695,540),10)
					count+=1
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
					#print(selected_card)
					#print(boolean_dict)
				elif boolean_dict["c7"]==False:
					selected_card.remove(player1_cards[6])
					#print(selected_card)
					#print(boolean_dict)
					count-=1
			elif 751<mx<844 and 400<my<520 and count<3:
				if boolean_dict["c8"]==False:
					boolean_dict["c8"]=True
				else:
					boolean_dict["c8"]=False
				if boolean_dict["c8"]==True:
					pygame.draw.circle(screen,NEON,(795,540),10)
					count+=1
					selected_card.append(player1_cards[7])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[7])
					count-=1
			elif 851<mx<944 and 400<my<520 and count<3:
				if boolean_dict["c9"]==False:
					boolean_dict["c9"]=True
				else:
					boolean_dict["c9"]=False
				if boolean_dict["c9"]==True:
					pygame.draw.circle(screen,NEON,(895,540),10)
					count+=1
					selected_card.append(player1_cards[8])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[8])
					count-=1
			elif 951<mx<1044 and 400<my<520 and count<3:
				if boolean_dict["c10"]==False:
					boolean_dict["c10"]=True
				else:
					boolean_dict["c10"]=False
				if boolean_dict["c10"]==True:
					pygame.draw.circle(screen,NEON,(995,540),10)
					count+=1
					selected_card.append(player1_cards[9])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[9])
					count-=1
			elif 1051<mx<1144 and 400<my<520 and count<3:
				if boolean_dict["c11"]==False:
					boolean_dict["c11"]=True
				else:
					boolean_dict["c11"]=False
				if boolean_dict["c11"]==True:
					pygame.draw.circle(screen,NEON,(1095,540),10)
					count+=1
					selected_card.append(player1_cards[10])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[10])
					count-=1
			elif 1151<mx<1244 and 400<my<520 and count<3:
				if boolean_dict["c12"]==False:
					boolean_dict["c12"]=True
				else:
					boolean_dict["c12"]=False
				if boolean_dict["c12"]==True:
					pygame.draw.circle(screen,NEON,(1195,540),10)
					count+=1
					selected_card.append(player1_cards[11])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[11])
					count-=1
			elif 1251<mx<1344 and 400<my<520 and count<3:
				if boolean_dict["c13"]==False:
					boolean_dict["c13"]=True
				else:
					boolean_dict["c13"]=False
				if boolean_dict["c13"]==True:
					pygame.draw.circle(screen,NEON,(1295,540),10)
					count+=1
					selected_card.append(player1_cards[12])
					if count==3:
						swap_cards()
						boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
					
				else:
					selected_card.remove(player1_cards[12])
					count-=1
			


			elif 1351<mx<1444 and 400<my<520 and count<3:
				if boolean_dict[c4]==False:
					boolean_dict[c4]=True
				else:
					boolean_dict[c4]=False
				if boolean_dict[c4]==True:
					pygame.draw.circle(screen,NEON,(1395,540),10)
					count+=1
					selected_card.append(player1_cards[3])
					if count==3:
						swap_cards()
						count=1
						selected_card=[]
				#pygame.display.flip()
				#boolean_dict[c1]=True
			

					
				else:
					selected_card.remove(player1_cards[3])
					count-=1
			elif 600<mx<690 and 249<my<370:
				blind_card=draw_card(stock_pile)
				card6=pygame.image.load("Cards/"+str(blind_card)+".png")
				card6=pygame.transform.scale(card6,(95,120))
				screen.blit(card6,(700,250))
				pygame.display.flip()

				#pygame.draw.circle(screen,(0,0,0),(647,227),10)
				#pygame.display.flip()
			if 700<mx<794 and 249<my<370:
				pygame.draw.circle(screen,(0,0,0),(747,227),10)
				if len(discarded_cards)==0:
					discarded_cards.append(blind_card)
				else:
					discarded_cards[0]=blind_card
				#print(selected_card)
				#print(discarded_cards)
				if len(selected_card)==1:
					
					
					#cardblind=selected_card[0]
					blind_card=selected_card[0]
					swap_cards_pick(selected_card[0],discarded_cards[0])
					selected_card=[]
					move_count+=1
					
					card2=pygame.image.load("Cards/"+str(blind_card)+".png")
					card2=pygame.transform.scale(card2,(95,120))
					boolean_dict={"c1":False,"c2":False,"c3":False,"c4":False,"c5":False,"c6":False,"c7":False,"c8":False,"c9":False,"c10":False,"c11":False,"c12":False,"c13":False}
					count=1
					"""temp2=card71d
					player1_cards[player1_cards.index(card70s)]=temp2"""


					#print(player1_cards)
				#pygame.display.flip()
			 
			pygame.display.flip()
			#pygame.draw.circle(screen,NEON,(xcolour,540),10)
			#print(selected_card)
	#print(blind_card)
	player1_turn()
	#print(2)


#screen.blit(win,(0,0))
#pygame.display.flip()
		
				




