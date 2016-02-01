;; scheme daily homework 3
;; name: Cory Jbara
;; date: January 27, 2015

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_dailies/d3/paradigms_d3.scm")
(use-modules (ice-9 paradigms_d3))

;; double
(define double 
  (lambda (n)
	(doubleHelper n n)
  )
)

(define doubleHelper
  (lambda (n1 n2)
    (cond
      ((zero? n2) n1)
      (else (doubleHelper (add1 n1) (sub1 n2)))
    )
  )
)

;; tests!
(display (double 9))
(display "\n")

(display (double 2))
(display "\n")

(display (double 45))
(display "\n")

;; correct output:
;;   $ guile d3.scm
;;   18
;;   4
;;   90

