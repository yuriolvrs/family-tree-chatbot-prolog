% Dynamic Declarations
:- dynamic parent/2, sibling/2, brother/2, sister/2, father/2, mother/2, parents/3.
:- dynamic grandmother/2, grandfather/2, grandparent/2, child/2, children/4, grandchild/2.
:- dynamic daughter/2, son/2, auntle/2, uncle/2, nibling/2, aunt/2, nephew/2, niece/2.
:- dynamic female/1, male/1.
:- dynamic are_related/2, siblings/2, cousins/2.

% Rules
sibling(X, Y) :-   
    parent(Z, X), 
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    sibling(X, Y),
    male(X).

sister(X, Y) :-
    sibling(X, Y),
    female(X).

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

parents(X, Y, Z) :-
    parent(X, Z),
    parent(Y, Z),
    female(X),
    male(Y),
    X \= Y.

grandparent(X, Y) :-
    parent(Z, Y),
    parent(X, Z).

grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

child(X, Y) :-
    parent(Y, X).

children(A, B, C, D) :-
    parent(D, A),
    parent(D, B),
    parent(D, C),
    A \= B,
    A \= C,
    B \= C.

grandchild(X, Y) :-
    parent(Y, Z),
    parent(Z, X).

daughter(X, Y) :-
    child(X, Y),
    female(X).

son(X, Y) :-
    child(X, Y),
    male(X).

auntle(X, Y) :-
    siblings(X, Z),
    parent(Z, Y).

uncle(X, Y) :-
    auntle(X, Y),
    male(X).

aunt(X, Y) :-
    auntle(X, Y),
    female(X).

nibling(X, Y) :-
    (aunt(Y, X);
    uncle(Y, X));
    (parent(Z, X),
    siblings(Y, Z)).

nephew(X, Y) :-
    nibling(X, Y),
    male(X).

niece(X, Y) :-
    nibling(X, Y),
    female(Y).

siblings(X, Y) :-
    sibling(X, Y);
    sibling(Y, X).

cousins(X, Y) :-
    siblings(A, B),
    (parent(A, X), parent(B, Y); parent(A, Y), parent(B, X)),
    X \= Y.

are_related(X, Y) :-
    parent(X, Y);
    parent(Y, X);
    siblings(X, Y);
    grandparent(X, Y);
    grandparent(Y, X);
    auntle(X, Y);
    auntle(Y, X);
    cousins(X, Y);
    cousins(Y, X).
