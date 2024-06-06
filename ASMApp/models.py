from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):#abstractuser creates fields to existing table 
	rt = [
		(0,'Guest'),
		(1,'Student'),
		(2,'Teacher'),
	]
	eid = models.CharField(max_length=20)
	role_type = models.IntegerField(default=0)
	pf_image=models.ImageField(upload_to='profiles/',default='static/images/logo.png')
class TeacherProfile(models.Model):
	g = [
		("k","Select Your Gender"),
		('M',"Male"),
		("F","Female")
		]
	b = [
		('G','----- Select Branch -----'),
		('CSE','Computer Science and Engineering'),
		('ECE','Electrical and Communication Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('CIVIL','Civil Engineering'),
	]
	tage = models.IntegerField()
	tgr = models.CharField(max_length=5,default='k',choices=g)
	tbranch = models.CharField(max_length=6,default='G',choices=b)
	tsubject = models.CharField(max_length=50)
	texpr = models.IntegerField()
	tdesg = models.CharField(max_length=50)
	tstatus = models.BooleanField(default=0)
	tch = models.OneToOneField(User,on_delete=models.CASCADE) #one teacher has one id so they can create one time only so we used onetoone fileld
    #on_delete=models.CASCADE i.e if we delete teacher data in user table it will delete automatically in all tables
class StudentProfile(models.Model):
	sg = [
		("h","Select Your Gender"),
		('M',"Male"),
		("F","Female")
	]
	b = [
		('G','----- Select Branch -----'),
		('CSE','Computer Science and Engineering'),
		('ECE','Electrical and Communication Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('CIVIL','Civil Engineering'),
	]
	y = [
		('0','----- Select Year -----'),
		('1','1st Year'),
		('2','2nd Year'),
		('3','3rd Year'),
		('4','4th Year'),
	]
	stage = models.IntegerField()
	sgr = models.CharField(max_length=5,default='h',choices=sg)
	sbranch = models.CharField(max_length=6,default='G',choices=b)
	syear = models.CharField(max_length=3,default='0',choices=y)
	sstatus = models.BooleanField(default=0)
	std = models.OneToOneField(User,on_delete=models.CASCADE)
class AssignmentT(models.Model): #teacher assignment
	y = [
		(0,'----- Select Year -----'),
		(1,'1st Year'),
		(2,'2nd Year'),
		(3,'3rd Year'),
		(4,'4th Year'),
	]
	b = [
		('G','----- Select Branch -----'),
		('CSE','Computer Science and Engineering'),
		('ECE','Electrical and Communication Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('CIVIL','Civil Engineering'),
	]
	anm = models.IntegerField()
	aname = models.CharField(max_length=50)
	ayear = models.IntegerField(default=0,max_length=5,choices=y)
	abranch = models.CharField(default='G',max_length=6,choices=b)
	asubject = models.CharField(max_length=50)
	adesc = models.CharField(max_length=250)
	astartdate = models.DateField()
	aenddate = models.DateField()
	amarks = models.IntegerField(default=10)
	astatus = models.BooleanField(default=0)
	atch = models.ForeignKey(User,on_delete=models.CASCADE)#teacher can create many assgnments so we use foreign key
class AssignmentSt(models.Model):
	c = [
		('0','Start'),
		('1','Activated'),
		('2','Submitted'),
		('3','Verified'),
	]
	d = [
		('4','Not Verified'),
		('3','Verified'),
	]
	asd = models.ForeignKey(AssignmentT,on_delete=models.CASCADE)#assignment id student can have many assignments so we used foreign key and assignment is present in assignment teacher tablke so we using it
	san = models.CharField(max_length=50)
	ssubject = models.CharField(max_length=150)
	scrted = models.DateField()
	ssubd = models.DateField(null=True)
	samarks = models.IntegerField(default=0)
	sactive = models.CharField(max_length=5,choices=c,default='0')
	sarev = models.CharField(max_length=150,null=True)#stu review
	sastre = models.CharField(max_length=200,null=True)#teacher review for stu assignmen
	stactive = models.CharField(default='4',choices=d,max_length=3)
	ssd = models.ForeignKey(User,on_delete=models.CASCADE)	#which stu is submitting data so we using one id we use user beacuse roletype i.e student present in user 