"""ONSITEDAY2"""
def main():
    """ONSITEDAY2"""
    start = 0
    total = 0
    var_list = [float(i) for i in input().split()]
    for i in var_list:
        total += abs(i-start)
        start = i
    print("%.2f"%total)
main()
