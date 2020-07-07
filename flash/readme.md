#### FlashDisco! | A flascard app

## What this app is about

FlashDisco! is an app for making an rehearsing flashcards. Flashcards are cards with a front stating a question (or concept) and a back stating an answer (or definition). Flashcards can be used to rehearse answering those questions and thus are a tool for learning.

## App demo

! [Demo](https://github.com/tdijkmans/FlashCards/tree/master/flash/readme-assets/Flashcards.gif)

## Used technologies and concepts

- Django 3 as ORM for the SQLite DB
- Bootstrap 4 for as UI
- HTML/CSS and JS for interacting with the flashcards

## Goals for this project

This was my first Django project (early 2020) and I challenged myself to learn app building by making a 'minimum viable product' for flashcards. This entailed:

- Defining models
- Defining model relationships
- Designing UI that execute CRUD operations to the SQLite DB
- Coding a UI using that serves the user in using flashcards
- Learning and practicing , Bootstrap, HTML, CSS and Javascript along the way

## User Stories

- As a page visitor, I want to be able to sign up as a user
- As a user, I want to be able to create new Card Decks
- As a user, I want to be able to create new Flash Cards (Q+A's) belonging to Card Decks
- As a user, I want to edit existing Flash Cards (Q+A's)
- As a user, I want to be able to reheares Flash Cards, i.e. browse through their Questions (frontside) and flip them to reveal their Answers (backside)
- As a user, I want to be able to see all my Card Decks and their related Flash Cards
- As s user, I want to be able to save Card Decks to My Study Set
- As s user, I want to be able to seeand remove Card Decks from My Study Set

## If you want to install

- Install Django 3 and Bootstrap 4 (pip install) as dependencies
- In the root folder containing manage.py: python manage.py runserver
