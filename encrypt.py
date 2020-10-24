#password check
#deneme
import sys
from password import *
check_algorithm=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+r+s+t+u+v+y+z+x
letter = {}
lettercalc=0
final="\n\n\n\n\n\n\nEncrypted Text: "

if check_algorithm == 311:
    input_msg = "testdoc"
    engel=len(input_msg)
    akis_kodu=0
    first_letter = ord(input_msg[akis_kodu])-96



    if first_letter < alpha:
        first_letter=first_letter+26
        first_letter_number=first_letter-alpha
        print(first_letter_number)
        letter[akis_kodu]=chr(first_letter_number+96)
    else:
        first_letter_number=first_letter-alpha
        print(first_letter_number)
        letter[akis_kodu]=chr(first_letter_number+96)

    #ikinci harf hazırlanışı
    akis_kodu=akis_kodu+1
    devam_letter=ord(input_msg[akis_kodu])-96


    if devam_letter < first_letter_number:
            devam_letter=devam_letter+26
            main_letter=devam_letter-first_letter_number
            print(main_letter)
            letter[akis_kodu]=chr(main_letter+96)
    else:
            main_letter=devam_letter-first_letter_number
            print(main_letter)
            letter[akis_kodu]=chr(main_letter+96)


    while True:
        akis_kodu=akis_kodu+1
        if akis_kodu == engel:

            while True:

                if lettercalc==akis_kodu:
                    print(final)
                    sys.exit()
                else:
                    final=final+letter[lettercalc]
                    lettercalc=lettercalc+1


        devam_letter=ord(input_msg[akis_kodu])-96

        if devam_letter < main_letter:
            devam_letter=devam_letter+26
            main_letter=devam_letter-main_letter
            print(main_letter)
            letter[akis_kodu]=chr(main_letter+96)

        else:
            main_letter=devam_letter-main_letter
            print(main_letter)
            letter[akis_kodu]=chr(main_letter+96)

else:
    print("password file wrong")
