/* ==================== FACTS ==================== */
male(jack).
male(oliver).
male(ali).
male(james).
male(simon).
male(harry).

female(helen).
female(sophie).
female(jess).
female(lily).

parent_of(jack, jess).
parent_of(jack, lily).
parent_of(helen, jess).
parent_of(helen, lily).
parent_of(oliver, james).
parent_of(sophie, james).
parent_of(jess, simon).
parent_of(ali, simon).
parent_of(lily, harry).
parent_of(james, harry).

/* ==================== RULES ==================== */
father_of(X, Y) :- male(X), parent_of(X, Y).
mother_of(X, Y) :- female(X), parent_of(X, Y).

grandfather_of(X, Y) :- male(X), parent_of(X, Z), parent_of(Z, Y).
grandmother_of(X, Y) :- female(X), parent_of(X, Z), parent_of(Z, Y).

sibling_of(X, Y) :- parent_of(Z, X), parent_of(Z, Y), X \= Y.

brother_of(X, Y) :- male(X), sibling_of(X, Y).
sister_of(X, Y) :- female(X), sibling_of(X, Y).

uncle_of(X, Y) :- brother_of(X, Z), parent_of(Z, Y).
aunt_of(X, Y) :- sister_of(X, Z), parent_of(Z, Y).

ancestor_of(X, Y) :- parent_of(X, Y).
ancestor_of(X, Y) :- parent_of(X, Z), ancestor_of(Z, Y).