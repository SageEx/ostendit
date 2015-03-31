import logging
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from Article.models import *
from django.http import HttpResponse
from forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage ,EmptyPage
from django.core.urlresolvers import reverse
import hashlib
import random

#page1 = None

#current_page = None

# Create your views here.
@csrf_exempt
def edit_profile(request):
    try : 
        if request.session['id'] != "" : 
	    if(request.session['user_permission']==-1) : 
		return HttpResponseRedirect('/articles/all/')	
            if 'save' in request.POST :
                myuser = MyUser.objects.get(user_name=request.session['id'])
                setattr(myuser,"user_email",request.POST['email'])
                setattr(myuser,"user_college",request.POST['college']) 
                request.session['user_email'] = request.POST['email']
                request.session['user_college'] = request.POST['college']  
                myuser.save()
                return HttpResponseRedirect('/edit/')
	             
            if 'submit_password' in request.POST :
            	myuser = MyUser.objects.get(user_name=request.session['id'])
            	old_pwd = getattr(myuser, "user_password")
            	curr_pwd = request.POST.get('curr_password')
            	new_pwd = request.POST.get('new_password')
            	conf_pwd = request.POST.get('conf_password')
            
            	if old_pwd != curr_pwd:
                	error = "Current Password not matched"
                	return render_to_response('Software/edit_profile.html', {'error': error,'email':request.session['user_email'],'college':request.session['user_college'],'myuser':myuser,'user_permission':request.session['user_permission']})

            	if new_pwd != conf_pwd:
                	error = "New and Confirm Password not matched"
                	return render_to_response('Software/edit_profile.html', {'error': error,'email':request.session['user_email'],'college':request.session['user_college'],'myuser':myuser,'user_permission':request.session['user_permission']})

            	if (len(new_pwd) < 8) or (len(new_pwd) > 25):
                	error = "Password must be atleast 8 characters long and max 25 characters"
                	return render_to_response('Software/edit_profile.html', {'error': error,'email':request.session['user_email'],'college':request.session['user_college'],'myuser':myuser,'user_permission':request.session['user_permission']})

            	error = ""

            	setattr(myuser, "user_password", new_pwd)
            	myuser.save()
            	request.session['error'] = new_pwd
            	return HttpResponseRedirect('/edit/')
	
            else :  
                myuser = MyUser.objects.get(user_name=request.session['id'])            
                return render_to_response('Software/edit_profile.html',{'email':request.session['user_email'],'college':request.session['user_college'],'myuser':myuser,'user_permission':request.session['user_permission']})

        else : 
            return render_to_response('Software/login.html',{'data':"Enter the deta",'error':True})
    except :
        request.session['id'] = ""
        return render_to_response('Software/login.html',{'data':"Enter the Details",'error':True})   

@csrf_exempt
def logout(request) :
    try :
        request.session['id'] = ""
        request.session['user_name'] = ""
        request.session['user_email'] = ""
	request.session['user_permission'] = ""
        request.session['user_college'] = ""
        request.session['security_question'] = ""
        request.session['security_answer'] = ""  
        request.session['error'] = ""   
        return HttpResponseRedirect('/login/')
    except :        
        return HttpResponseRedirect('/login/')

@csrf_exempt
def login(request) :
     
    try : 
        if request.session['id'] != "" : 
            return HttpResponseRedirect('/articles/all/')
        else : 
		
            if 'login' in request.POST : 
                data = MyUser.objects.get(user_name=request.POST['userName'],user_password=request.POST['userPassword'])
                request.session['id'] = getattr(data,"user_name")
                request.session['user_name'] = getattr(data,"user_name")
                request.session['user_email'] = getattr(data,"user_email")
                request.session['user_college'] = getattr(data,"user_college")
                request.session['security_question'] = getattr(data, "security_question")
                request.session['security_answer'] = getattr(data, "security_answer")  
                request.session['number_posts'] = "5"
		request.session['user_permission'] = getattr(data,"user_permission") 
		return HttpResponseRedirect('/articles/all/')			                
	    return render_to_response('Software/login.html',{'data':"Enter the details",'error':False})
		
    except :
        request.session['id'] = ""
        return render_to_response('Software/login.html',{'data':"Wrong Username or Password",'error':True})

@csrf_exempt
def articles(request):
        language = 'en-gb'
        session_lanuage = 'en-gb'

        if 'lang' in request.COOKIES : 
                language = request.COOKIES['lang']

        if 'lang' in request.session : 
                session_language = request.session['lang']
        
        return render_to_response('article.html',
                                 { 'articles' : Article.objects.all(),
                                   'language' : language,
                                   'session_language' : session_language })

#def article(request ,article_id=1) : 
#        return render_to_response('article.html',
#                                 { 'articles' : Article.objects.get(id=article_id) })

@csrf_exempt
def language(request , language='en-gb') : 
        response = HttpResponse("setting language to %s" % language)

        reponse.set_cookie('lang',language)

        response.session['lang'] = language

        return response

@csrf_exempt
def create(request):
   
        if request.session['id'] != "" :
	    if request.session['user_permission'] == 2 or request.session['user_permission'] == -1 : 				
		return HttpResponseRedirect('/articles/all/')

            if request.POST:
                #form = ArticleForm()
                #args['title'] = request.POST['title']
                #args['body'] = request.POST['body']
                #args['tag'] = request.POST['tag']
                #data = form.save()
                #setattr(data, "title", request.POST['title'])
                #setattr(data, "body", request.POST['post'])
                #if 'tag' in request.POST:
                 #   setattr(data, "tag", request.POST['tag'])
                #if 'file' in request.POST:
                 #   setattr(data, "docfile", request.FILES['file'])
                #setattr(data, "author",request.session['id'])
                #data.save()
                #args.save()
                title = request.POST.get('title');
                bdy =  request.POST.get('post');
                if 'tag' in request.POST:
                    tags = request.POST.get('tag');
                else:	
                    tags = ""
                if 'file' in request.FILES:
                    docfile = request.FILES.get('file');
                else:
                    docfile = None
                auth = request.session['id'];
                data = Article(title=title, body=bdy, tag=tags, author=auth, doc=docfile)                          
                setattr(data, "key", True)
                data.save()
                return HttpResponseRedirect('all/') 
        
            else : 
                form = ArticleForm()
                args = {}
                args.update(csrf(request))
                args['form'] = form
                return render_to_response('Software/create_article.html',{'user_permission':request.session['user_permission']})
        else : 
            return HttpResponseRedirect('/login/')
                           

@csrf_exempt
def start(request):
    form = ArticleForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('Software/create_article.html',{'user_permission':request.session['user_permission']},args)        

@csrf_exempt
def main(request):
    #articles = Article.objects.all().order_by("-created")
    #global page1   
    try :
        if request.session['id'] != "" : 
            num = request.session['number_posts']            
            num = int(num)                     
            articles = Article.objects.filter(key = True)    
            paginator = Paginator(articles,num)   
            page1 = paginator.page(1)
            author = request.session['id']
            return render_to_response("Software/list.js",{'posts' : page1,'author':author, 'num':num,'user_permission':request.session['user_permission']},context_instance=RequestContext(request))
        else :
            return HttpResponseRedirect('/login/')
    except :
        return HttpResponseRedirect('/login/')

@csrf_exempt
def save_article(request):
    
    try :
        if request.session['id'] != ""  :                               #loaded just after saving an article
            form  = ArticleForm(request.POST)
            form.save()
            #articles = Article.objects.all().order_by("-created")
            #global page1
            articles = Article.objects.all()
            num = request.session['number_posts']
            num = int(num)
            paginator = Paginator(articles,10)
            page1 = paginator.page(1)
            gue = request.session['guest']
            return render_to_response("Software/list.js",{'posts' : page1, 'num':num, 'guest':gue})
        else :
            return HttpResponseRedirect('/login/')
    except :
        return HttpResponseRedirect('/login/')

@csrf_exempt    
def main_offset(request,  offset):                              #direct to requested page from offset
    
    try :   
        if request.session['id'] != "" :            
            #global page1
            author = request.session['id']
            articles = Article.objects.filter(key = True)
            num = request.session['number_posts']
            num = int(num)
            number = int(offset)
            paginator = Paginator(articles,num)
            if number <= paginator.num_pages :                          #if number is valid (less than maximum pages in paginator)
                page1 = paginator.page(number)
                num1 = page1.__len__()
            else : 
                page1 = paginator.page(1)                           #direct user to first page
            return render_to_response("Software/list.js",{'posts' : page1,'author':author, 'num':num, 'num1':num1,'user_permission':request.session['user_permission']})
        else :
            return HttpResponseRedirect('/login/')
    except : 
        return HttpResponseRedirect('/login/')

@csrf_exempt
def load_article(request,offset) :                                                                 #here offset marks the id of article
    
        if request.session['id'] != "" :
            form = CommentsForm()
            args = {}
            args.update(csrf(request))

            if 'like' in request.POST :                                                                #person has clicked on 'like'                 
                #if page1 is None :                                                                 #page 1 can be null now
                        #return HttpResponseRedirect('/articles/all')        
                #else : 
                _offset = int(offset)
                #curent_page = Article.objects.filter(article_id = offset)
                current_page = Article.objects.get(id = _offset)                
                setattr(current_page,"likes",getattr(current_page,"likes")+1)
                current_page.save()                        
                #offset = int(offset) - 1
                #comments = getattr(current_page,"all_stored_comments")        
                comment_list = []
                comment_list = Comments.objects.filter(parent_article_id = offset)                        
                return HttpResponseRedirect('/load/'+offset)
                #return render_to_response("Software/display_article.html",{'post':current_page,'form':form,'comments':comments, 'author':current_page.author}, 
                #context_instance=RequestContext(request))
        
            elif 'comments' in request.POST : 
                form = CommentsForm(request.POST)
                current_comment = form.save()        
                #logging.WARNING(current_comment.comment)                   
                current_page = Article.objects.get(id = offset)
                setattr(current_comment,"parent_article_id",offset)
                current_comment.save()
                comment_list = []
                comment_list = Comments.objects.filter(parent_article_id = offset)
                #current_page.add_comments(current_comment)
                return HttpResponseRedirect('/load/'+offset)
                #return render_to_response("Software/display_article.html",{'post':page1.object_list[offset],'form':form,'comments':current_comment})

            elif 'delete' in request.POST:
                current_page = Article.objects.get(id = offset)
                author = current_page.author
                
                if request.session['id'] == author :
                    setattr(current_page, "key", False)
                    current_page.save()
		    #Ask for confirmation	
                    return HttpResponseRedirect('/articles/all')

                else :
                    return HttpResponseRedirect('/load/'+offset)

            elif 'edit' in request.POST:

                current_page = Article.objects.get(id = offset)
                author = getattr(current_page, "author")

                if author == request.session['id']:
                    body = getattr(current_page, "body")
                    key = True
                    offset = int(offset)                
                    current_page = Article.objects.get(id = offset)
                    comment_list = []
                    comment_list = Comments.objects.filter(parent_article_id = offset)    
                    return render_to_response("Software/display_article.html", {'post':current_page,'form':form,'comments':comment_list, 'key':key, 'key1':True,'user_permission':request.session['user_permission']}, context_instance=RequestContext(request))

                else:
                    return HttpResponseRedirect('/load/'+offset)

            elif 'edit_post' in request.POST:

                current_page = Article.objects.get(id = offset)
                author = getattr(current_page, "author")

                if author == request.session['id']:
                    setattr(current_page, "body", request.POST['edit_post'])
                    current_page.save()
                    comment_list = []
                    comment_list = Comments.objects.filter(parent_article_id = offset)
                    return render_to_response("Software/display_article.html", {'post':current_page,'form':form,'comments':comment_list, 'key':False, 'key1':True,'user_permission':request.session['user_permission']}, context_instance=RequestContext(request))

            else :
                #if page1 is None :                                                                 #page 1 can be null now
                        #return HttpResponseRedirect('/articles/all')
                #else : 
                #offset = int(offset)-1
                #offset = int                
                #if offset < 3 : 
                #        current_page = page1.object_list[offset]
                #        #comments = getattr(current_page,"all_stored_comments")        
                #       comments = Comments.objects.all()                
                #        return render_to_response("Software/display_article.html",{'post':page1.object_list[offset],'form':form,'comments':comments})
                #else :
                #        return HttpResponseRedirect('/articles/all')
                offset = int(offset)
                #current_page = Article.objects.get(article_id = offset)
                current_page = Article.objects.get(id = offset)
                comment_list = []
                comment_list = Comments.objects.filter(parent_article_id = offset)
                if request.session['id'] == getattr(current_page, "author") :
                    key1 = True
                else:
                    key1 = False

                return render_to_response("Software/display_article.html",{'post':current_page,'form':form,'comments':comment_list, 'key':False, 'key1':key1,'user_permission':request.session['user_permission']}, context_instance=RequestContext(request))

        else :
            return HttpResponseRedirect('/login/')

@csrf_exempt
def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''

	args = {}
        args.update(csrf(request))
	articles = Article.objects.filter(title__icontains=search_text, key=True).order_by('title') | Article.objects.filter(tag__icontains=search_text, key=True)
	return render_to_response('Software/ajax_search.html', {'articles':articles,'user_permission':request.session['user_permission']})

@csrf_exempt
def change_password(request):

    if request.session['id'] != "" :
        
        if request.POST :
            data = MyUser.objects.get(user_name=request.session['user_name'])
            old_pwd = getattr(data, "user_password")
            curr_pwd = request.POST.get('curr_password')
            new_pwd = request.POST.get('new_password')
            conf_pwd = request.POST.get('conf_password')
            
            if old_pwd != curr_pwd:
                error = "Current Password not matched"
                return render_to_response('Software/change_password.html', {'error': error,'user_permission':request.session['user_permission']})

            if new_pwd != conf_pwd:
                error = "New and Confirm Password not matched"
                return render_to_response('Software/change_password.html', {'error': error,'user_permission':request.session['user_permission']})

            if (len(new_pwd) < 8) or (len(new_pwd) > 25):
                error = "Password must be atleast 8 characters long and max 25 characters"
                return render_to_response('Software/change_password.html', {'error': error,'user_permission':request.session['user_permission']})

            error = ""

            setattr(data, "user_password", new_pwd)
            data.save()
            request.session['error'] = new_pwd
            return HttpResponseRedirect('/edit/')
        else:
            error = ""
            return render_to_response('Software/change_password.html')

@csrf_exempt
def passwd(request):
    if request.session['id'] == "":
        return render_to_response("Software/forgotPassword.html", {'user_permission':request.session['user_permission']})

@csrf_exempt
def forgot_password(request):
    
    try:
        if request.session['id'] == "":
            
            username = request.POST.get('username')
            data = MyUser.objects.get(user_name=username)
            sec_ans = request.POST.get('sec_ans')
            sec_ques = request.POST.get('sec_ques')

            if sec_ques == getattr(data, "security_question") and sec_ans == getattr(data, "security_answer"):
                request.session['forgot_user'] = username
                return render_to_response("Software/for_chg_passwd.html", {'user_permission':request.session['user_permission']})
            else:
                return HttpResponseRedirect('/login/')

    except:
        return HttpResponseRedirect('/te1/')

@csrf_exempt
def forgot_change_password(request):
    
    if request.session['id'] == "":

        if request.POST:
            userName = request.session['forgot_user']
            data = MyUser.objects.get(user_name=userName)
            new_pwd = request.POST.get('for_new_password')
            conf_pwd = request.POST.get('for_conf_password')

            if new_pwd != conf_pwd:
                error = "New and Confirm Password not matched"
                return render_to_response('Software/for_chg_passwd.html', {'error': error})

            if (len(new_pwd) < 8) or (len(new_pwd) > 25):
                error = "Password must be atleast 8 characters long and max 25 characters"
                return render_to_response('Software/for_chg_passwd.html', {'error': error,'user_permission':request.session['user_permission']})

            error = ""

            setattr(data, "user_password", new_pwd)
            data.save()
            request.session['id'] = userName
            return HttpResponseRedirect('/login/')
        else:
            error = ""
            return render_to_response('Software/for_chg_passwd.html', {'error': error,'user_permission':request.session['user_permission']})

@csrf_exempt
def add_user(request):

    if request.session['id'] != "":
	if request.session['user_permission'] == 2 or request.session['user_permission'] == -1 : 				
		return HttpResponseRedirect('/articles/all')

        if request.POST:
            userName = request.POST['username']
            password = request.POST['password']
            college = request.POST['college']
            email = request.POST['email']
            user = MyUser(user_name=userName, user_password=password, user_college=college, user_email=email)

            if (len(password) < 8) or (len(password) > 25):
                error = "Password must be atleast 8 characters long and max 25 characters"
                return render_to_response('Software/addUser.html', {'user_permission':request.session['user_permission']})
            user.save()
            return HttpResponseRedirect('/articles/all/')

        else:
            return render_to_response("Software/addUser.html")
    
    else:
        return HttpResponseRedirect('/login/')
@csrf_exempt 
def front(request):
	try : 
		if(request.session['id']!=""):
			return render_to_response('Software/fabricsort.html', {'user_permission':request.session['user_permission']}) 
		else : 
			return HttpResponseRedirect('/login/')
	except : 
		return HttpResponseRedirect('/login/')
@csrf_exempt
def guest(request):
	request.session['id'] = "gue"
	request.session['user_permission'] = -1
	return HttpResponseRedirect('/articles/all/')
