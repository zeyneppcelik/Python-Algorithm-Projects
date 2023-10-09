import os

print("Welcome to the secret auction program!!")

def auction(bid_records):
    bid_amount=0
    winner=''
    for key in bid_records:
        if bid_records[key]>bid_amount:
            bid_amount=bid_records[key]
            winner=key
    print(f"Winner is {winner} and bid {bid_amount}")

bidding_finished='yes'

while bidding_finished=='yes':
    name=input("What is your name?\n")
    bid=int(input("What is your bid\n"))
    bids={}
    bids[name]=bid
    bidding_finished=input("Are there other users who want to bid?(yes or no)\n").lower()
    os.system('cls')

auction(bids)

