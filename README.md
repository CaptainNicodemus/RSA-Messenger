![Vulcans](./Readme%20images/Logo_White.png)
# RSA Messenger - Read me

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)


* [Updates](#updates)
* [Setup](#setup)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Team Members: Nicodemus Robles, Trey Tolleson, Mandi Renae Palencia, Roman Iles

2. What you’re creating?

* Team Vulcan is creating a custom RSA Encryption Messenger as a simple solution for secure private messaging accessible for everyone.

3. Who you’re doing it for, your audience (may be same as the previous question)?

* We are hopping that business and people trying to communicate  securely via the internet could use our system  

4. Why you’re doing this, the impact or change you hope to make?

* A lot of people don't understand how to encrypt their data, with this tool, we are trying to make it easy and secure

## Technologies

**RSA Encryption** :  is a public-key cryptosystem that is widely used for secure data transmission. An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret. Messages can be encrypted by anyone, via the public key, but can only be decoded by someone who knows the prime numbers.

​	Here are some RSA links		

				- [RSA Basics](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
				- [Youtube Explains RSA](https://www.youtube.com/watch?v=wXB-V_Keiu8)

  Information on prime number generation and primality testing:
        - [Generation of primes](https://en.wikipedia.org/wiki/Generation_of_primes)
        - [Fermat primality test](https://en.wikipedia.org/wiki/Primality_test#Fermat_primality_test)
        
## Features

- **Features:** What will be the initial features in this first sprint.

- - **Give each feature a name.**
  - **Describe what it does and who or what uses it.**
  - **What user stories correspond to this feature.**

* Sprint 1: Encryption Algorithm
  1. To begin our project, we will need to create an Encryption Algorithm for simple messages.
  2. As a message app user, we would like an RSA messenger with a strong encryption sequence.

To-do list:

- Add padding to RSA
- Make desktop app



## Updates

### Sprint 1 - v0.01

​	**Nicodemus Robles** 

C++ RSA encryptor and decryptor - ./crypt/\C++ RSA key generator\cmake-build-debug\C___RSA_key_generator.exe

- This sprint I added  a C++ RSA encryptor and decryptor. In its current state, the program can only encrypt/decrypt hard coded int's and the key's aren't strong . 

I also added some RSA documents for reference.

Next steps: Convert RSA into python and add better inputs

​	**Trey Tolleson**

Sprint 1 data base: [vertabelo](https://my.vertabelo.com/public-model-view/Zf7pHePlY5ezN1TGpDdgoPh01FjFGnjADZO8yimuoBF2M0fmjokpquRsEuDpIsFb?x=1883&y=2162&zoom=0.4632)

- Database model for messaging between users within application. Can be converted to query language to be used in chosen DBM

Next step is to find a suitable database service to deploy model into.

​	**Mandi Renae Palencia** 

Sprint 1 chat: I've made a simple chatroom app that uses socket programming in python to connect a server and client. Multiple users can join. The code can be found in the "socket" folder.

We plan on creating a desktop application with this simple base. The code connects two nodes on a network to communicate to each other. The socket or node listens on a particular port at an IP, while the other socket searches to form a connection.

Next steps: Integrate RSA with chat application and use Universal Windows Platform to create an official desktop application.

**Roman Iles**

​    Prime generation: 
​      implemented the fermat primality test in python:  [fermat_primality.py](https://bitbucket.org/cs3398s21vulcans/uss-enterprise/src/master/primes/fermat_primality.py)
​        

- The base RSA algorithm operates with prime numbers, which will us erandomly generated prime numbers. Because this process is best done with algorithms that only "probably" generate prime numbers, we have primality tests to validate.
  
- Next up would be feeding this primality test (it has its flaws) into some other primality tests to up the validation. I would also work on a prime-number generator. There are several proven generators that have high probabilities of generating primes, but validation is still important.



## Updates

### Sprint 2

 **Mandi Palencia**

 Dicussed logistics of how to connect the GUI to the ecryption and database code. We wanted to add a feature to the chat for attaching an image so I have added a new feature that allows the user to add an image from their local directory, albeit the code to send the image to the server needs to be worked on.

​	**Trey Tolleson**

Created a database to hold user information on Microsoft Azure Cloud Services. There is a working piece of code to add users to database in Database Model/ main.py.
The Next Step is to integrate the database with Mandi's server and client application.

## Setup

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

## Status
Project is: _in progress_

## Inspiration
Add here credits. Project inspired by..., based on...

## Contact 
* Repo owner or admin
* Other community or team contact
