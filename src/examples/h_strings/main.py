#main program
import strings

def main():
    strings.string_params("test")
    
    str1 = "python"
    strings.string_loop_w_while(str1)

    str2 = "python"
    strings.string_loop_w_for_range(str2)
    
    str3 = "four score and seven years ago"
    split_text = str3.split()

    print (split_text)

    val = 'w' * 5
    print (val)

main()