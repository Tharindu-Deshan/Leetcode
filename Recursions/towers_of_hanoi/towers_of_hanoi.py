def TOH(n,from_peg,aux_peg,to_peg):
    if(n==1):
        print(f"move disk number {n} from {from_peg} to {to_peg}")
        return 
    TOH(n-1,from_peg,to_peg,aux_peg)
    print(f"move disk number {n} from {from_peg} to {to_peg}")
    TOH(n-1,aux_peg,from_peg,to_peg) 
    

TOH(2,"A","B","C")