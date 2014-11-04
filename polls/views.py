#import django libraries
import django
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Template, Context
from django.http import HttpResponseRedirect
from django import forms

#importing additional libraries
import datetime

#importing tables---
from polls.models import Restaurant, Person, Dish, Choice
#importing forms---
import polls.forms_DK


#Global variables
global cut_hour
now = datetime.datetime.now()
#cut_hour = now.replace(hour=16, minute=0, second=0, microsecond=0)
#for testing
cut_hour = now.replace(hour=01, minute=0, second=0, microsecond=0)

cut_hour_12 = cut_hour.strftime("%I:%M:%p")


def get_timer():
    timer = datetime.datetime.now()
    timer_split = str(timer).split()
    return timer_split


def main_site(request):
    body = "Welcome,  please vote and select your order"
    d = {"body": body}
    #return render_to_response('initial_page.html', d)
    return render(request, "home.html", d)


def vote(request):
    #we need to check if its before 4pm
    if request.method == "POST":
        form = polls.forms_DK.NameForm(request.POST)
        if form.is_valid():
            your_email = form.cleaned_data["your_email"]
            ratio = str(form.cleaned_data["ratio"])
            django.setup()

            timer_split = get_timer()
            dater = timer_split[0]
            hrs = timer_split[1]
            # we check if the user exists in the database.
            try:
                checking_email = Person.objects.get(email=your_email)
            except:
                address = "registration/"
                return HttpResponseRedirect(address)

            #Checking if its before 4pm cut_hour
            if datetime.datetime.now() < cut_hour:
                print "you can still vote"
                #quering to see if the person voted
                date_query = Choice.objects.filter(date_vote=dater)
                voted = False
                for i in date_query:
                    if i.person_id == checking_email.id:
                        voted = True
                        print "you voted"

                # action if he voted or not
                if voted is False:

                    cc = Choice(date_vote=dater, time_vote=hrs, restaurant_vote_id=ratio, person_id=checking_email.id)
                    cc.save()
                    address = "thank/?email="+your_email+"/"
                    return HttpResponseRedirect(address)
                elif voted is True:
                    message = "you already voted tomorrow try again"
                    return render(request, "thanks.html", {"message": message})

                address = "thank/?email="+your_email+"/"
                return HttpResponseRedirect(address)

            else: # if its after cut_hour
                message = "its after time, talk to your PA he might take your order"
                return render(request, "thanks.html", {"message": message})


    #regular empty forms render for the first time.
    else:
        form = polls.forms_DK.NameForm()
    django.setup()
    all_restaurants = Restaurant.objects.all()

    message = "select the restaurant of your choice before: " + str(cut_hour_12)
    return render(request, "vote_form.html", {"message": message, "all_restaurants": all_restaurants, "form": form})


def registration(request):
    if request.POST:
        form = polls.forms_DK.FormRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/polls/vote/")
    else:
        form = polls.forms_DK.FormRegistration()
        message = "we couldnt find your information, please fill the forms."
        dic = {"message": message, "form": form}
        return render(request, "vote_form.html", dic)


def thank(request):
    req_email = request.GET["email"]

    c = {"message": "thanks for voting " + req_email}
    return render(request, "thanks.html", c)


def restaurant_menu(request, rest_id="0"):
    response = HttpResponse()
    try:
        p = Restaurant.objects.get(id=rest_id)
        response.write("<html><body>")
        response.write("<p>name of the restaurant</p>")
        response.write(p.name)
        response.write("</body></html>")

    except Restaurant.DoesNotExist:
        response.write("restaurant not found")
    return response


def order(request):
    if datetime.datetime.now() > cut_hour:
        i = datetime.datetime.now()
        date = str("%s-%s-%s") % (i.year, i.month, i.day)
        try:
            #Choice.objects.filter(date_vote=date)
            q_date = Choice.objects.filter(date_vote=date)
            #todo max is not working properly!!! aggregate function should be implemented here
            chosen_restaurant = max(q_date)

            #this is how we can get the max
            #but we need to return a choice object

            # dir = {}
            # for j in q_date:
            #     try:
            #         dir[j.restaurant_vote] = dir[j.restaurant_vote]+1
            #     except:
            #         dir[j.restaurant_vote] = 1
            # chosen_restaurant = max(dir)
            # chosen_restaurant = Restaurant.objects.get(name=chosen_restaurant)

        except:
            message = "no one voted, talk to your PA "
            return render(request, "thanks.html", {"message": message})

        if request.method == "POST":
            form = polls.forms_DK.FormDishes(request.POST, restaurant_id=chosen_restaurant.restaurant_vote.id)
            #todo do we want to make the user choose dish just once, or we let them change their minds? or same as voting for the restaurant
            if form.is_valid():
                your_email = form.cleaned_data["your_email"]
                ratiooo = str(form.cleaned_data["ratiooo"])

                timer_split = get_timer()
                dater = timer_split[0]
                hrs = timer_split[1]

                person = Person.objects.get(email=your_email)
                cc = person.choice_set.filter(date_vote=dater)[0]
                cc.time_dish = hrs
                cc.dish_id = ratiooo
                res_instance = Restaurant.objects.get(id=chosen_restaurant.restaurant_vote_id)
                cc.restaurant_winner = res_instance
                cc.save()

                message = "your dish has been order"
                return render(request, "thanks.html", {"message": message})
        else:
            restaurant = Restaurant.objects.get(id=chosen_restaurant.restaurant_vote_id)
            form = polls.forms_DK.FormDishes(restaurant_id=restaurant.id)
            return render(request, "vote_form.html", {"message": "select your dish", "form": form})
    else:
        message = "we don't know hows the winner yet, we will find out at: "+str(cut_hour_12)
        return render(request, "thanks.html", {"message": message})


def orders_to_go(request):
    #todo display the information of the restaurant and the user food selection, only 2 hours after cut_hours
    try:
        d = {}
        list_of_choices = Choice.objects.filter(date_vote=get_timer()[0])
        d["lc"] = list_of_choices

        win_rest = list_of_choices[0].restaurant_winner

        res_res = list_of_choices.filter(restaurant_winner_id=win_rest)[0]
        res = Restaurant.objects.get(id=res_res.id)

        d["message"] = "Restauran: "+str(res)+\
                       " adress: "+str(res.adress)+\
                       " phone: "+str(res.phone_number)
        return render(request, "orders_to_go.html", d)
    except:
        return render(request, "thanks.html", {"message": "no orders to process yet"})


def statistics(request):
    return render(request, "statistics.html", {"message": "statistics are part of phase 2"})
