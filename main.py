def compute_share():
    """
    Computes the total amount of shares to give an investor based on the percentage of shares the company is offering the investor
    """

    
    shares = []
    shareholders_num = int(input("How many Shareholders are we looking at?: "))
    for shareholder in range(1, shareholders_num+1):
        shares.append(int(input(f"What is the percentage of Shares for shareholder {shareholder}: ")))

    investor = int(input("What is the percentage of shares you're looking to accommodate?: "))
    for share in shares:
        sh2give = investor / 100 * share
        new_share = share - sh2give
        print(new_share)


compute_share()
