from django.shortcuts import render, redirect
from .models import (School, Principle, Category,
                     Status, SubCounty, Capacity,)
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.views import View
from django.http import HttpResponseRedirect
# from django.contrib.auth import set_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import (PrincipleForm, CategoryForm, StatusForm,
                    SubcountyForm, SchoolForm, CapacityForm,
                    # FilesUploads
                    )
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
User = get_user_model()


class SchoolsListView(View):
    # @method_decorator(login_required)

    def get(self, request, *args, **kwargs):
        queryset = School.objects.all().order_by('name')
        paginator = Paginator(queryset, 25)
        page = request.GET.get('page')

        try:
            schools = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            schools = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            schools = paginator.page(paginator.num_pages)
        context = {
            "title": "schools",
            "data": schools,
            "page": page,
        }
        return render(request=request,
                      template_name="main/lists/Schoolist.html",
                      context=context)


class SubcountyListView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        queryset = SubCounty.objects.all()
        paginator = Paginator(queryset, 10)
        page = request.GET.get('page')
        try:
            subs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            subs = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            subs = paginator.page(paginator.num_pages)
        context = {
            "title": "Sub Counties",
            "data": subs,
            "page": page
        }
        return render(request,
                      'main/lists/Subcountylist.html',
                      context=context)


class PrinciplesListView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        queryset = Principle.objects.all()
        paginator = Paginator(queryset, 25)
        page = request.GET.get('page')
        try:
            prn = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            prn = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            prn = paginator.page(paginator.num_pages)
        context = {
            "title": "Principle list",
            "data": prn,
            "page": page,
            "total": queryset.count()
        }
        return render(request,
                      'main/lists/Principleslist.html',
                      context=context)


class CategoriesListView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        paginator = Paginator(queryset, 10)
        page = request.GET.get('page')
        try:
            ctg = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            ctg = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            ctg = paginator.page(paginator.num_pages)
        return render(request,
                      'main/lists/Categorieslist.html',
                      {"title": "Categories", "data": ctg, "page": page})


class StatusListView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        queryset = Status.objects.all()
        paginator = Paginator(queryset, 10)
        page = request.GET.get('page')
        try:
            sts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            sts = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            sts = paginator.page(paginator.num_pages)
        context = {
            "title": "Status",
            "data": sts,
            "page": page
        }
        return render(request,
                      'main/lists/statuslist.html',
                      context=context)


class CapacityListView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        queryset = Capacity.objects.filter(school=pk)
        school = School.objects.get(id=pk)
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page')
        try:
            capt = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            capt = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            capt = paginator.page(paginator.num_pages)

        return render(request,
                      'main/lists/capacitylist.html',
                      {"data": capt, "school": school, "page": page})


class PrincipleView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = PrincipleForm()
        return render(request, 'main/Forms/PrincipleForm.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            principle = PrincipleForm(request.POST)
            Principle.objects.create(
                username=principle.data["username"],
                last_name=principle.data["last_name"],
                tsc=principle.data["tsc"],
                telNo=principle.data["telNo"],
                first_name=principle.data["first_name"],
            )
            context = {
                "Message": "Success",
                "Status": True,
            }
        except Exception as e:
            context = {
                "Message": str(e),
                "Status": False
            }
        # print(request.POST)
        return render(request=request,
                      template_name="main/Forms/PrincipleForm.html",
                      context=context)


class CategoryView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,
                      'main/Forms/CategoryForm.html', {"form": CategoryForm()})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            category = CategoryForm(request.POST)
            Category.objects.create(
                name=category.data['name'],
                description=category.data['description'],
            )
            context = {
                "Message": "Success",
                "Success": True
            }
        except Exception as e:
            context = {
                "Message": str(e),
                "Success": False
            }

        # this should re
        return render(request,
                      template_name='main/Forms/CategoryForm.html',
                      context=context)


class StatusView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,
                      'main/Forms/StatusForm.html', {'form': StatusForm()})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            status = StatusForm(request.POST)
            Status.objects.create(
                name=status.data['name'],
                description=status.data['description']
            )
            context = {
                'Message': "Success",
                'Success': True
            }
        except Exception as e:
            context = {
                'Message': str(e),
                'Success': False
            }

        return render(request, 'main/Forms/StatusForm.html', context=context)


class SubcountyView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,
                      'main/Forms/SubcountyForm.html',
                      {'form': SubcountyForm()})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            subcounty = SubcountyForm(request.POST)
            SubCounty.objects.create(
                name=subcounty.data['name'],
            )
            context = {
                'Message': 'Success',
                'Success': True
            }
        except Exception as e:
            context = {
                'Message': str(e),
                'Success': False
            }
        return render(request,
                      'main/Forms/SubcountyForm.html',
                      context=context)


class SchoolView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,
                      'main/Forms/SchoolsForm.html',
                      {'form': SchoolForm()})

    @method_decorator(login_required)
    def post(slef, request, *args, **kwargs):
        try:
            school = SchoolForm(request.POST)
            # print(school.data)
            School.objects.create(
                name=school.data['name'],
                knecCode=school.data['knecCode'],
                principle=Principle.objects.get(id=school.data['principle']),
                subCounty=SubCounty.objects.get(id=school.data['subCounty']),
                category=Category.objects.get(id=school.data['category']),
                status=Status.objects.get(id=school.data['status']),
                sType=school.data['sType'],
                streams=school.data['streams'],
                enrollment=school.data['enrollment'],
            )
            context = {
                'Message': 'Success',
                'Success': True
            }
        except Exception as e:
            context = {
                'Message': str(e),
                'Success': False
            }
        return render(request, 'main/Forms/SchoolsForm.html', context=context)


class CapacityView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,
                      'main/Forms/CapacityForm.html',
                      {'form': CapacityForm()})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            capacity = CapacityForm(request.POST)
            Capacity.objects.create(
                school=School.objects.get(id=capacity.data['school']),
                year=capacity.data['year'],
                gender=capacity.data['gender'],
                amount=capacity.data['amount']
            )
        except Exception as e:
            raise e
        return redirect('/')


# class UploadsView(View):
#     """docstring for Uploads"""

#     def get(self, request, *args, **kwargs):
#         return render(request, 'main/Uploads.html', {'form': FilesUploads()})

#     def post(self, request, *args, **kwargs):
#         try:
#             # uploads = FilesUploads(request.POST)
#             # # print(request.FILES['file'])
#             # # data_str = csv.reader(request.FILES['file'])
#             # print([i for i in csv.reader(uploads.data['file'])])
#             # # with open(uploads.data['file']) as csvfile:
#             # spamreader = csv.reader(uploads.data['file'], delimiter=',')
#             # for row in spamreader:
#             #     print(row)
#             context = {
#                 'Message': extract(itemloc=2),
#                 'Success': True
#             }
#         except Exception as e:
#             context = {
#                 'Message': str(e),
#                 'Success': False
#             }
#         return render(request, 'main/Uploads.html', context=context)


class SchoolDetailView(View):

    # @method_decorator(login_required)
    def get(self, request, pk):
        queryset = School.objects.get(id=pk)
        capacity = Capacity.objects.filter(school=pk)
        return render(request,
                      'main/details/SchoolDetail.html',
                      {"data": queryset, "capacity": capacity})


class PrincipleDetailView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        return render(request,
                      'main/details/principledetails.html',
                      {"data": Principle.objects.get(id=pk)})


class SchoolUpdateView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        data = {
            "school": School.objects.get(id=pk),
            "categories": Category.objects.all(),
            "statuses": Status.objects.all(),
            "principles": Principle.objects.all(),
            "subcounties": SubCounty.objects.all(),
            "sTypes": [
                ('PR', 'Primary'),
                ('SC', 'Secondary'),
            ]
        }
        return render(request, 'main/updates/schoolsupdate.html', context=data)

    @method_decorator(login_required)
    def post(self, request, pk):
        form = SchoolForm(request.POST)
        sch = School.objects.get(id=pk)
        sch.name = form.data['name']
        sch.knecCode = form.data['knecCode']
        sch.principle = Principle.objects.get(id=form.data['principle'])
        sch.subCounty = SubCounty.objects.get(id=form.data['subCounty'])
        sch.category = Category.objects.get(id=form.data['category'])
        sch.status = Status.objects.get(id=form.data['status'])
        sch.sType = form.data['sType']
        sch.streams = form.data['streams']
        sch.enrollment = form.data['enrollment']
        sch.save()
        return redirect('/school/detail/' + str(pk))


class SubcountyUpdateView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        return render(request,
                      'main/updates/subcountyupdate.html',
                      {"data": SubCounty.objects.get(id=pk)})

    @method_decorator(login_required)
    def post(self, request, pk):
        sub = SubCounty.objects.get(id=pk)
        form = SubcountyForm(request.POST)
        sub.name = form.data['name']
        sub.code = form.data['code']
        sub.save()
        return redirect('/subcounties/list/')


class CapacityUpdate(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        queryset = Capacity.objects.get(id=pk)
        school = School.objects.get(id=queryset.school.id)
        return render(request,
                      'main/updates/capacityupdate.html',
                      {"data": queryset,
                       "school": school,
                       "genderlist": [
                           ("B", "Boys"),
                           ("G", "Girls")
                       ]
                       }
                      )

    @method_decorator(login_required)
    def post(self, request, pk):
        # allow change of year and remove change of gender
        # change of year check if the year exists first for the specific school
        cap = Capacity.objects.get(id=pk)
        capacity = CapacityForm(request.POST)
        cap.gender = capacity.data['gender'],
        cap.amount = capacity.data['amount']
        cap.save()
        return redirect('/capacity/list/' + str(cap.school.id))


class StatusUpdateView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        return render(request,
                      'main/updates/statusupdate.html',
                      {"data": Status.objects.get(id=pk)})

    @method_decorator(login_required)
    def post(self, request, pk):
        sts = Status.objects.get(id=pk)
        form = StatusForm(request.POST)
        sts.name = form.data['name']
        sts.save()
        return redirect('/status/list/')


class CategoryUpdateVIew(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        return render(request,
                      'main/updates/categoryupdate.html',
                      {"data": Category.objects.get(id=pk)})

    @method_decorator(login_required)
    def post(self, request, pk):
        cat = Category.objects.get(id=pk)
        form = CategoryForm(request.POST)
        cat.name = form.data['name']
        cat.save()
        return redirect('/category/list/')


class PrincipleUpdateView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        return render(request,
                      'main/updates/principlesupdate.html',
                      {"data": Principle.objects.get(id=pk)})

    @method_decorator(login_required)
    def post(self, request, pk):
        prn = Principle.objects.get(id=pk)
        form = PrincipleForm(request.POST)
        prn.tsc = form.data["tsc"]
        prn.telNo = form.data["telNo"]
        prn.first_name = form.data["first_name"]
        prn.last_name = form.data["last_name"]
        # prn.username = form.data["username"]
        prn.email = form.data["email"]
        prn.save()
        return redirect('/principle/list/')


class CapacityDeleteView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        try:
            cap = Capacity.objects.get(id=pk)
            school = cap.school.id
            cap.delete()
        except Exception as e:
            raise e
        return redirect('/capacity/list/' + str(school))


class SchoolDeleteView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        School.objects.get(id=pk).delete()
        return redirect('/')


class SubcountyDeleteView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        SubCounty.objects.get(id=pk).delete()
        return redirect('/subcounties/list/')


class StatusDeleteView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        Status.objects.get(id=pk).delete()
        return redirect('/status/list/')


class CategoryDeleteView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        Category.objects.get(id=pk).delete()
        return redirect('/category/list/')


class PrincipleDeleteView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        Principle.objects.get(id=pk).delete()
        return redirect('/principle/list/')


class SignUp(View):

    def post(self, request):
        # print(request.POST)
        user = User.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
        )
        user.set_password(request.POST['password'])
        user.save()
        user = authenticate(username=user.username, password=user.password)
        login(request, user)
        return redirect("/")


class Login(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('/subcounty/stat/')

    def post(self, request):
        logout(request)
        # username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
        return redirect('/subcounty/stat/',
                        context={"data": "login failed"})

#  stats


class TotalSchoolsPerSubCounty(View):

    @method_decorator(login_required)
    def get(self, request):
        try:
            sub_names = []
            total_schools = []
            for sub in SubCounty.objects.all().values("id", "name"):
                sub_names.append(sub["name"])
                total_schools.append(
                    School.objects.filter(subCounty=sub["id"]).count())
            tp_labels = []
            tp_values = []
            for tp in Status.objects.all():
                tp_labels.append(tp.name)
                tp_values.append(School.objects.filter(status=tp.id).count())
            cat_labels = []
            cat_values = []
            for cat in Category.objects.all():
                cat_labels.append(cat.name)
                cat_values.append(School.objects.filter(category=cat.id).count())
            # print(request.user)
            return render(request, 'main/Stats/schoolsubcounty.html',
                      {
                          "sub": {"labels": sub_names,"values": total_schools},
                          "tp": {"labels": tp_labels, "values": tp_values},
                          "cat": {"labels": cat_labels,"values": cat_values}
                      })
        except Exception as e:
            print(str(e))
            return redirect("/")
