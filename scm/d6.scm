;; scheme daily homework 6
;; name: Cory Jbara
;; date: February 3, 2016

(use-modules (ice-9 debugging traps) (ice-9 debugging trace))

(define atom?
	(lambda (x)
		(and (not (null? x)) (not (pair? x)))))

(define sum*
	(lambda (ttup)
		(cond
			((null? ttup) 0)
			((atom? (car ttup)) (+ (car ttup) (sum* (cdr ttup))))
			(else (+ (sum* (car ttup)) (sum* (cdr ttup))))
		)
	)
)

	; YOUR CODE HERE :-)


;(install-trap (make <procedure-trap>
;                            #:procedure sum*
;                            #:behaviour (list trace-trap trace-until-exit)))

;; tests!
(display (sum* '((5)) ))
(display "\n")

(display (sum* '((0) ((0) ((5))) ((0) ((10)))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7)))) ((0) ((10) ))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7) ) ((8) ))) ((0) ((10) ))) ))
(display "\n")

;; correct output:
;;   $ guile d6.scm
;;   5
;;   15
;;   22
;;   30

