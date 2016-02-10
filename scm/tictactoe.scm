;; scheme tictactoe homework
;; name: Cory Jbara
;; date: February 10, 2016

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_tictactoe/paradigms_ttt.scm")
(use-modules (ice-9 paradigms_ttt))
(use-modules (ice-9 debugging traps) (ice-9 debugging trace))

;; greatest
;; return the greatest value in a tup, e.g., (1 3 2) -> 3
(define greatest
	(lambda (tup)
		(cond
			((null? (cdr tup)) (car tup))
			((> (car tup) (car (cdr tup))) (greatest (cons (car tup) (cdr (cdr tup)))))
			(else (greatest (cdr tup)))
		)    
	)
)

;; positionof
;; you may assume that the given tup actually contains n
;; e.g., (positionof 23 (1 52 23 9)) -> 3
(define positionof
	(lambda (n tup)
		(cond 
			((eq? n (car tup)) 1)
			(else (+ 1 (positionof n (cdr tup))))
		)
	)
)

;; value
;; given a game state, return the value of that state:
;; 10 if it's a win
;; -10 if it's a loss
;; 0 if it is either a draw or not an ending state
(define value
	(lambda (p)
		(lambda (gs)
			(cond 
				((win? p gs) 10)
				(else 
					(cond 
						((win? (other p) gs) -10)
						(else 0)
					)
				)
			)
		)
	)
)

(define count
	(lambda (x)
		(cond ((null? x) 0) (else	(+ 1 (count (cdr x)))))))

(define state?
	(lambda (x)
		(cond
			((eq? (count x) 9) #t)
			(else #f)
		)
	)
)

(define sum*-g
	(lambda (ttup f)
		(cond
			((null? ttup) 0)
			((state? ttup) (f ttup))
			(else (+ (sum*-g (car ttup) f) (sum*-g (cdr ttup) f)))
		)
	)
)
;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
	(lambda (p gt)
		(cond
			((null? (cdr gt)) (car gt))
			(else (decodePos gt (positionof (greatest (valueList p (cdr gt))) (valueList p (cdr gt)))))
		)
	)
)

(define valueList 
	(lambda (p gt)
		(cond
			((null? gt) '())
			(else (cons (sum*-g (car gt) (value p)) (valueList p (cdr gt))))
		)
	)
)

;; Takes a game tree and a position of the next move and returns that state
(define decodePos
	(lambda (gt pos)
		(cond
			((eq? pos 0) (caar gt))
			(else (decodePos (cdr gt) (- pos 1)))
		)
	)
)
;(install-trap (make <procedure-trap>
;                            #:procedure valueList
;                            #:behaviour (list trace-trap trace-until-exit)))

;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
(display "Current State:     ")
(display (car (onegametree)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (onegametree)))
(display "\n")

;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

