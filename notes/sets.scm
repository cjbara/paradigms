(define member?
	(lambda (a lat)
		(cond
			((null? lat) #f)
			((eq? (car lat) a) #t)
			((member? a (cdr lat)) #t)
			(else #f)
		)
	)
)

(define set?
	(lambda (l)
		(cond 
			((null? l) #t)
			((member? (car l) (cdr l)) #f)
			(else (set? (cdr l)))
		)
	)
)

(define makeset
	(lambda (l)
		(cond
			((null? l) '())
			((member? (car l) (cdr l)) (makeset (cdr l)))
			(else (cons (car l) (makeset (cdr l))))
		)
	)
)

(define firsts
	(lambda (l)
		(cond
			((null? l) '())
			(else (cons (caar l) (firsts (cdr l))))
		)
	)
)

(define fun?
	(lambda (l)
		(set? (firsts l))
	)
)

(define reverseFun
	(lambda (l)
		(cond
			((null? l) '())
			(else 
				(cons 
					(cons (reverseOrderedPair (car l))
					(reverseFun (cdr l)))
				)
			)
		)
	)
)

(define reverseOrderedPair
	(lambda (p)
		((cons (car (cdr p)) (cons (car p) '())))
	)
)

(display (makeset '(1 2 3 4 5 2 3 2 2 4 1 3)))
(display "\n")
(display (reverseFun '((0 3) (1 2) (0 1) (2 6))))
(display "\n")
