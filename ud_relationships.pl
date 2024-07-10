:- dynamic parent/2, siblings/2, grandmother/2, grandfather/2, grandparent/2, daughter/2, son/2, aunt/2, uncle/2.
:- dynamic female/1, male/1, brother/2, sister/2, mother/2, father/2, relatives/2, nibling/2, grandchild/2, cousins/2.

mother(X,Y):- parent(X,Y),female(X), X\=Y.
father(X,Y) :- parent(X,Y),male(X), X\=Y.
siblings(X,Y):- parent(Z,X),parent(Z,Y), X\=Y, Y\=Z, X\=Z.
child(X,Y) :- parent(Y,X), X\=Y.
sister(X,Y) :- siblings(X,Y),female(X), X\=Y.
brother(X,Y) :- siblings(X,Y),male(X), X\=Y.
grandparent(X,Z):- parent(X,Y),parent(Y,Z), X\=Y, X\=Z, Y\=Z.
grandmother(X,Y):- grandparent(X,Y),female(X), X\=Y.
grandfather(X,Y):- grandparent(X,Y),male(X), X\=Y.
grandchild(X,Y) :- grandparent(Y,X), X\=Y.
daughter(X,Y):-female(X),parent(Y,X), X\=Y.
son(X,Y):- male(X),parent(Y,X), X\=Y.
aunt(X,Z):-female(X),siblings(X,Y),parent(Y,Z), X\=Y, X\=Z, Y\=Z.
uncle(X,Z):-male(X),siblings(X,Y),parent(Y,Z), X\=Y, X\=Z, Y\=Z.
nibling(Z,X) :- siblings(X,Y),parent(Y,Z), X\=Y.
cousins(X,Y) :- siblings(PX,PY), parent(PX,X), parent(PY,Y), X\=Y.
relatives(X,Y) :- siblings(X, Y), X\=Y.
relatives(X,Y) :- parent(X, Y), X\=Y.
relatives(X,Y) :- child(X, Y), X\=Y.
relatives(X,Y) :- grandmother(X, Y), X\=Y.
relatives(X,Y) :- grandfather(X, Y), X\=Y.
relatives(X,Y) :- daughter(X, Y), X\=Y.
relatives(X,Y) :- son(X, Y), X\=Y.
relatives(X,Y) :- aunt(X, Y), X\=Y.
relatives(X,Y) :- uncle(X, Y), X\=Y.
relatives(X,Y) :- grandparent(X, Y), X\=Y.
relatives(X,Y) :- nibling(X, Y), X\=Y.
relatives(X,Y) :- grandchild(X, Y), X\=Y.
relatives(X,Y) :- cousins(X, Y), X\=Y.