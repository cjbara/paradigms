;; this is how to load external modules in scheme
(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_dailies/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; Cory Jbara

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output: #f
;; (copy the output you saw here)
;;
;; explanation:
;; (use as many lines as necessary, just add more comments)
;; This code will check if the (stuffing poatoe ham) list is an atom, which is false.
;; (cdr q) = ((gravy) (stuffing potatoes ham) peas))
;; (cdr (cdr q)) = ( (stuffing potatoes ham) peas))
;; (car (cdr (cdr q))) = ( (stuffing potatoes ham) )
;; Since this is not an atom, it returns #f
;; 


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; #t
;;
;; explanation:
;; This is the exact same code as the first, but it now checks if (stuffing potatoes ham) 
;; is a list atom, which it is
;; (cdr q) = ((gravy) (stuffing potatoes ham) peas))
;; (cdr (cdr q)) = ( (stuffing potatoes ham) peas))
;; (car (cdr (cdr q))) = ( (stuffing potatoes ham) )
;;


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;; turkey
;;
;; explanation:
;; This code is an if statement that checks if (car q) = (turkey) is an atom? which it is
;; Because the statement is true, it prints out (car q) which is turkey
;;

