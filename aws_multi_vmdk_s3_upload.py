import os

file_name=input("Input file part name (No numbers, no extension) :")
bucket=input("Input AWS Bucket name: ")
end_point = input("Input the total number of files: ")
file_path = input("Input file path of file_parts (No trailing \'\\\'): ")

command_name = None
print("Uploading file parts...")
for i in range(0,int(end_point)):
    upload_num = str(i+1)
    if (i+1) < 100 :
        if(i+1) < 10:
            upload_num = "00"+ str(upload_num)
        else:
            upload_num = "0"+str(upload_num)
    
    code=os.system(('cmd /c aws s3 cp \"' +file_path +"\\" + file_name + upload_num +".vmdk\" " + bucket))
    print()
    code=code+1
    if code ==0:
        print("Part " + upload_num + "Failed...")
        exit(code)
    print("Part " + upload_num + "/"+str(end_point) +"Completed")
print("Done..")
