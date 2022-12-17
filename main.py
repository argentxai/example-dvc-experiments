
#import dvc.api
import sys
sys.path.append('/home/karan/kj_workspace/kj_open_source/dvc/')
import dvc.api

rev = sys.argv[1] if len(sys.argv) == 2 else None

fs = dvc.api.DVCFileSystem(".", rev=rev)
for file in fs.find("/", detail=False, dvc_only=True):
    print(file)
    #print(fs.read_text(file))


