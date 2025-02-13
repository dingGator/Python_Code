import blind_auction_art

print(blind_auction_art.logo)
print("\n")
print("Welcome to the secret auction program. ")
# TODO-1: Ask the user for input
name = input("What is your name?:  " ).lower()
bid = int(input("What is your bid? "))

# TODO-2: Save data into dictionary {name: price}
bid_dict = {}

def add_to_dictionary(bidder_name, price):
    bid_dict[bidder_name] = price
#    print(bid_dict)

add_to_dictionary(bidder_name= name, price = bid)

# TODO-3: Whether if new bids need to be added

new_bid = True
while new_bid:

    new_bid_yes_or_no = input("Are there any  other bidders?  Type 'yes' or 'no'. ").lower()
    if new_bid_yes_or_no == "no":
        new_bid = False
    elif new_bid_yes_or_no == "yes":
        print("\n"*20)
        name = input("What is your name?:  ").lower()
        bid = int(input("What is your bid? "))
        add_to_dictionary(bidder_name= name, price = bid)

# TODO-4: Compare bids in dictionary
def compare_bids_in_dictionary(bid_dict):

    highest_bid = 0

    for bidder_name in bid_dict:
        #print("name " + bidder_name + "  bid " + str(bid_dict[bidder_name]))
        if highest_bid < bid_dict[bidder_name]:
            highest_bid = bid_dict[bidder_name]
            #print("name1 " + bidder_name + "  bid1 " + str(highest_bid_dict[bidder_name]))
    for win_name in bid_dict:
        if highest_bid == bid_dict[win_name]:
            print(f" {win_name} won with bid ${bid_dict[win_name]}.  ")


        #if highest_bid[bidder_name] < bid_dict[bidder_name]:
        #highest_bid[bidder_name] = bid_dict[bidder_name]

compare_bids_in_dictionary(bid_dict)