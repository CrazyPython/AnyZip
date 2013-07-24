from PythonCard import model,timer
from tkinter import Tk,tkFileDialog
import os,re,platform
alltypes =["lzma","bzip2","gzip"]
try:
    platform.linux_distribution
except:
    large = True
else:
    large = False
unableto = []
try:import lzma
except:unableto.append("lzma")
try:import bz2
except:unableto.append("bzip2")
try:import zlib
except:unableto.append("gzip")
def kind(url):
    if url.endswith('.zip'):
        return 'archive-zip'
    elif url.endswith('.bzip2'):
        return 'archive-bzip2'
    elif url.endswith('.xz') or url.endswith('.lzma'):
        return 'archive-lzma'
    elif url.endswith('.gzip'):
        return 'archive-gzip'
    elif re.search(r'+[a-z]|[A-Z]*'):
        return 'file'
    elif re.search('.exe|.dll|.batch'):
        return 'program'
    else:
        return 'folder'
def browse():
    root = Tk()
    root.withdraw()
    f = tkFileDialog.askopenfilename(parent=root,title=title, initialfile=default)
    if not f: return None
    return os.path.normpath(f)
def l():
    li = ['|','\\','-','/','-']
    it = li.__iter__()
    while True:
        try:
            yeild it.next()
        except StopIteration:
            continue
class Window(model.Background):
    def on_initialize(self):
        self.components.format.items = list(set(alltypes) ^ set(unableto))
        self.components.format.stringSelection = alltypes[0]
    def actiondec(f):
        @wraps(f)
        def wrap(*args,**kwargs):
          self.components.load.visible = True
          try:
              f(*args,*kwargs)
          except:
              try:f = open(self.components.url.text)
              except OSerror:self.components.msg.text = 'Error, Not Found or Encrypted(needs password)'
          self.components.load.visible = False
    def on_initialize(self):
        self.myTimer = timer.Timer(self.components.load, -1) # create a timer
        self.myTimer.Start(100)
    def on_browse_mouseClick(self,event):
        self.components.url.text = browse()
    def on_browse2_mouseClick(self,event):
        self.components.secondary.text = browse()
    def on_extract_mouseClick(self,event):
        f = self.components.url.text
        to = self.components.url.text
        if to.strip() == '':
            to = re.sub('.[a-z]|[A-Z]+','',f)
        z = zipfile.zip(f)
        if kind(f).startswith('archive-'):
            z.extractall(path=to,allowZip64=large)
        else:
            z.extractall(f.strip(to),path=to,allowZip64=large)
        z.close()
    #def on_zip_mouseClick(self,event): # in construction
        #zipfile.ZipFile(self.components.url.text,self.components.format.stringSelection)
    def on_run_mouseClick(self,event):
        t = self.components.url.text.strip()
        if secondary.strip():
            os.system(t+' '+secondary)
        else:
            os.system(t)
    def on_url_losefocus(self,event):
        t = self.components.url.text.strip()
        if t == '':
            self.components.view.enabled = False
            self.components.edit.enabled = False
            self.components.extract.enabled = False
            self.components.delete.enabled = False
            self.components.combine.enabled = False
        if kind(t).startswith('archive'):
            if kind(t).lstrip('archive-') in unableto:
                self.components.view.enabled = False
                self.components.edit.enabled = False
                self.components.extract.enabled = False
                self.components.delete.enabled = False
                self.components.combine.enabled = False
                self.components.msg.text = 'Unable to unzip'+kind(t).lstrip('archive-')+"Files"
            else:
                self.components.edit.enabled = False
                self.components.extract.enabled = True
                self.components.filenamedis.items = zipfile.zip(self.components.url.text).namelist()
        elif kind(t) == 'folder':
            self.components.zip.enabled = True
        elif kind(t) == 'program':
            self.components.run.enabled = True
            
    def on_secondary_losefocus(self,event):
        t = self.components.secondary.text.strip()
        self.components.combine.enabled = eval("t == ''")
    def on_load_timer(self,event):
        self.components.load = l()
