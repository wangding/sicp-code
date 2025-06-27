#lang racket
; 1.1.1 命名和环境（最简单的抽象）
(define size 2)
size
(* 5 size)
(define pi 3.14159)
(define radius 10)
(* pi (* radius radius))
(define circumference (* 2 pi radius))
circumference