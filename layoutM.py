import app
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def menu():

    print('\n\t===================== '+Fore.CYAN+'M_E_N_U '+Style.RESET_ALL+'========================')

    print('\n\t'+Fore.YELLOW+'['+Fore.YELLOW+'a'+Fore.YELLOW+']'+Fore.YELLOW+Style.RESET_ALL+'  DISPLAY MENU')
    print('\t'+Fore.YELLOW+'['+Fore.YELLOW+'b'+Fore.YELLOW+']'+Fore.YELLOW+Style.RESET_ALL+'  SEARCH')
    print('\t'+Fore.YELLOW+'['+Fore.YELLOW+'c'+Fore.YELLOW+']'+Fore.YELLOW+Style.RESET_ALL+'  INSERT')
    print('\t'+Fore.YELLOW+'['+Fore.YELLOW+'d'+Fore.YELLOW+']'+Fore.YELLOW+Style.RESET_ALL+'  UPDATE')
    print('\t'+Fore.YELLOW+'['+Fore.YELLOW+'e'+Fore.YELLOW+']'+Fore.YELLOW+Style.RESET_ALL+'  DELETE')

    ch = input('\nSelect Your Choice =>')
    
    if ch == 'a' or ch == 'A':  #display menu
        print('\n\t\t------======D I S P L A Y======------\n\n')
        app.M_display.showall()
        
    elif ch == 'b' or ch == 'B':    #search
        print('\n\t\t------======S E A R C H======------\n\n')
        print('\n\t |1| search using Item No ')
        print('\t |2| search using Item Name ')
        

        opt = input('Select Method to Search : ')

        if opt == '1':
            app.M_display.searchNo()

        elif opt == '2':
            app.M_display.searchName()



        else:
            app.M_display.searchNo()

    elif ch == 'c' or ch == 'C':    #insert
        print('\n\t\t------======I N S E R T======------\n\n')
        app.M_insert.insert()

    elif ch == 'd' or ch == 'D':
        print('\n\t\t------======U P D A T E======------\n\n')
        app.M_update
        print('\n\t= A = Change Item Name')
        print('\t= B = Change Amount')
        print('\t= C = Change Item No')
        
        opt = input('\nChoose an Option : ')
        
        if opt == 'a' or opt =='A':
            app.M_update.changeName()
        elif opt == 'b' or opt == 'B':
            app.M_update.changeAmount()
        elif opt == 'c' or opt == 'C':
            app.M_update.changeNo()
        else:
            print('Invalid Option, sorry')

    elif ch == 'e' or ch == 'E':
        print('\n\t\t------======D E L E T E======------\n\n')
        print('\n\t(1) Delete Using Item No')
        print('\t(2) Delete Using Item Name')
        opt = input('\nSelect an option : ')
        if opt == '1':
            app.M_delete.deleteNo()
        elif opt == '2':
            app.M_delete.deleteName()
        else:
            app.M_delete.deleteNo()
    else:
        print('Oops, Invalid choice')

            
            
            
#while True:
    
#    menu()
