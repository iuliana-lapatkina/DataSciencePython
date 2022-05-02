{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4df38c27",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "27d65255",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([[1, 2, 3, 3, 1],\n",
    "             [6, 8, 11, 10, 7]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bec43d71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 3 1]\n"
     ]
    }
   ],
   "source": [
    "a1 = a[0, :]\n",
    "print(a1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c4948349",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.0\n"
     ]
    }
   ],
   "source": [
    "print(np.mean(a1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "428141eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 6  8 11 10  7]\n"
     ]
    }
   ],
   "source": [
    "a2 = a[1, :]\n",
    "print(a2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b3ffd788",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8.4\n"
     ]
    }
   ],
   "source": [
    "print(np.mean(a2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "998e8cd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2.  8.4]\n"
     ]
    }
   ],
   "source": [
    "mean_a = np.array([np.mean(a1), np.mean(a2)])\n",
    "print(mean_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "16d31aa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-1.   0.   1.   1.  -1. ]\n",
      " [-2.4 -0.4  2.6  1.6 -1.4]]\n"
     ]
    }
   ],
   "source": [
    "a_centered = np.array([(a1 - np.mean(a1)), (a2 - np.mean(a2))] )\n",
    "print(a_centered)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "05fe3b5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8.0\n"
     ]
    }
   ],
   "source": [
    "a_centered_sp = np.dot(a_centered[0, :], a_centered[1, :])\n",
    "print(a_centered_sp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "67ac40f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0\n"
     ]
    }
   ],
   "source": [
    "N = len(a_centered[:][0])\n",
    "b =  np.subtract(a_centered_sp, (N - 1))\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35c43c37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
