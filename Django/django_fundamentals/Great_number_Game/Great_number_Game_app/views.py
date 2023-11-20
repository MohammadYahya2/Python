from django.shortcuts import render, redirect
import random

def root(request):
    correct_number = random.randint(1, 100)
    print(correct_number)
    request.session['correct_number'] = correct_number
    return render(request, 'index.html')
    

def check_guess(request):
    guess = int(request.POST['guess'])
    print(guess)
    correct_number = request.session['correct_number']
    messages = {
        'equal': "You guessed the correct number.",
        'low': "Too low",
        'high': "Too high"
    }

    if guess == correct_number:
        resl = messages['equal']


    elif guess < correct_number:
        resl = messages['low']

    else:
        resl = messages['high']
        

    return render(request, 'reselt.html', {'resl': resl})
