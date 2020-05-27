import os
import argparse
import sys
from merge_SBML import main_sbml
from main_annotation import main_analysis
from info_SBML import create_info
import json


### Creation of argument
def main():
    parser = argparse.ArgumentParser(description = "MerAnO") 
  
    parser.add_argument("-a", "--analyse", type = str, help = "folder in which the annotations files to be processed are located.Put the all path") 
    parser.add_argument("-m", "--merge", type = str, help = "folder in which the SBML files to merge are located. Put the all path")
	# parse the arguments from standard input 
    args = parser.parse_args()    
    m=args.merge
    a=args.analyse
    if a!=None or m!=None:
        SBML_files=get_files(m)
        annotation_files=get_files(a)
        check_files(SBML_files, ".xml")
        check_files(annotation_files, ".fa.emapper.annotations")
    else:
        print("Please mentionned option")
        sys.exit()
    
    if not os.path.exists('Results'):
        os.makedirs('Results') 
    
    else:
        continue

    if SBML_files >= 2:
        main_sbml(SBML_files)
        create_info(SBML_files)
    elif annotation_files != None and annotation_files < 6 :  
        if not os.path.exists('Storage'):
            os.makedirs('Storage')    
        if not os.path.isfile('Storage/modules.json'):
            with open("Storage/modules.json", mode='w') as f:
                f.write(json.dumps([], indent=4))    
        main_analysis(annotation_files)
    else:
        print("""
        Please put the authorized number of files :
            - More than 2 for merge option
            or 
            - Between 1 and 5 for analyze option
        """)
    

    
    


#    print(path)
    
#    print(files)

        

def get_files(arg):
    if arg!=None:
        if os.path.isdir(arg):
            if len(os.listdir(arg))!=0:
                user_files=[]
                for root, dir, files in os.walk(arg, topdown=False):
                    for name in files:
                        f = os.path.join(root,name)
                        user_files.append(f)
                return user_files
            else:
                print("Error : directory\"",arg,"\" is empty")
                sys.exit()
        else:
            print("Error : \"",arg,"\" does not exist!")
            sys.exit()
    else:
        return None

def check_files(filename, ext):
    if filename!=None:
        for f in filename:
            if f.endswith(ext):
                continue
            else:
                print("Error : \"", f,"\" is not ", ext, " file")
                sys.exit()



        ### Put files into a list

    


if __name__ == "__main__":
	main()
