/* =   FAMILY TREE IN PROLOG
   Contains: Grandparents, Parents, Children, 
             Grandchildren, Uncles, Aunts, Cousins = */

:- discontiguous male/1, female/1, parent/2.


% Grandparents Generation
male(john).
female(mary).

% Parents Generation
male(david).
female(sarah).
female(alice).      % David's sister (Aunt)
male(robert).       % David's brother (Uncle)

% Children Generation
male(michael).      % You
female(emma).       % Sister
male(james).        % Brother

% Grandchildren / Cousins Generation
female(sophie).     % Alice's daughter (Cousin)
male(liam).         % Robert's son (Cousin)
female(olivia).     % Another cousin

/* = PARENT RELATIONSHIPS = */

% Grandparents are parents of David, Alice, Robert
parent(john, david).
parent(mary, david).
parent(john, alice).
parent(mary, alice).
parent(john, robert).
parent(mary, robert).

% David and Sarah are parents of Michael, Emma, James
parent(david, michael).
parent(sarah, michael).
parent(david, emma).
parent(sarah, emma).
parent(david, james).
parent(sarah, james).

% Alice is mother of Sophie and Olivia
parent(alice, sophie).
parent(alice, olivia).

% Robert is father of Liam
parent(robert, liam).

/* = RULES = */

% Basic Gender Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

% Grandparents
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).
grandmother(X, Y) :- female(X), parent(X, Z), parent(Z, Y).
grandparent(X, Y) :- grandfather(X, Y).
grandparent(X, Y) :- grandmother(X, Y).

% Siblings
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

% Uncles and Aunts
uncle(X, Y) :- brother(X, Z), parent(Z, Y).
aunt(X, Y)  :- sister(X, Z),  parent(Z, Y).

% Cousins
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2), X \= Y.

% Grandchildren
grandchild(X, Y) :- parent(Y, Z), parent(Z, X).

% Ancestor and Descendant
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

descendant(X, Y) :- ancestor(Y, X).


family_member(X) :- male(X); female(X).

