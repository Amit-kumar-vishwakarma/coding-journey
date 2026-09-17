def calculate_marks(maths,eng,hindi,comp,history=0):
    print(f"maths={maths}")
    print(f"eng={eng}")
    print(f"hindi={hindi}")
    print(f"comp={comp}")
    print(f"historys={history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"total marks scored ={total_marks}")


# keywords  
calculate_marks(hindi=33,maths= 34,eng= 56, comp= 75, )
