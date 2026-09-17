def calculate_marks(maths,eng,hindi,comp,history=0):
    # history =0 is default argument

    #  maths hindi eng comp are required arguments 
    print(f"maths={maths}")
    print(f"eng={eng}")
    print(f"hindi={hindi}")
    print(f"comp={comp}")
    print(f"historys={history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"total marks scored ={total_marks}")



calculate_marks(23, 34, 56, 75, )
