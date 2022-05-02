{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8d0c500a",
   "metadata": {},
   "source": [
    "Задание 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "96afd382",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "1e90c565",
   "metadata": {},
   "outputs": [],
   "source": [
    "authors = pd.DataFrame({'author_id':[1, 2, 3],'author_name':['Тургенев', 'Чехов', 'Островский']},\n",
    "                       columns=['author_id', 'author_name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "8e379c2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author_id</th>\n",
       "      <th>author_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Чехов</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Островский</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   author_id author_name\n",
       "0          1    Тургенев\n",
       "1          2       Чехов\n",
       "2          3  Островский"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "authors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "ced1c38d",
   "metadata": {},
   "outputs": [],
   "source": [
    "book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],\n",
    "                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], \n",
    "                     'price':[450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "b29d908b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author_id</th>\n",
       "      <th>book_title</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Отцы и дети</td>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Рудин</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Дворянское гнездо</td>\n",
       "      <td>350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>Толстый и тонкий</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>Дама с собачкой</td>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3</td>\n",
       "      <td>Гроза</td>\n",
       "      <td>370</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3</td>\n",
       "      <td>Таланты и поклонники</td>\n",
       "      <td>290</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   author_id            book_title  price\n",
       "0          1           Отцы и дети    450\n",
       "1          1                 Рудин    300\n",
       "2          1     Дворянское гнездо    350\n",
       "3          2      Толстый и тонкий    500\n",
       "4          2       Дама с собачкой    450\n",
       "5          3                 Гроза    370\n",
       "6          3  Таланты и поклонники    290"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "book"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4f4603e",
   "metadata": {},
   "source": [
    "Задание 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "4957fe8d",
   "metadata": {},
   "outputs": [],
   "source": [
    " authors_price = pd.merge(authors, book, on = 'author_id', how = 'inner')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "9629e05b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author_id</th>\n",
       "      <th>author_name</th>\n",
       "      <th>book_title</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Отцы и дети</td>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Рудин</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Дворянское гнездо</td>\n",
       "      <td>350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>Чехов</td>\n",
       "      <td>Толстый и тонкий</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>Чехов</td>\n",
       "      <td>Дама с собачкой</td>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3</td>\n",
       "      <td>Островский</td>\n",
       "      <td>Гроза</td>\n",
       "      <td>370</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3</td>\n",
       "      <td>Островский</td>\n",
       "      <td>Таланты и поклонники</td>\n",
       "      <td>290</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   author_id author_name            book_title  price\n",
       "0          1    Тургенев           Отцы и дети    450\n",
       "1          1    Тургенев                 Рудин    300\n",
       "2          1    Тургенев     Дворянское гнездо    350\n",
       "3          2       Чехов      Толстый и тонкий    500\n",
       "4          2       Чехов       Дама с собачкой    450\n",
       "5          3  Островский                 Гроза    370\n",
       "6          3  Островский  Таланты и поклонники    290"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "authors_price"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0748d684",
   "metadata": {},
   "source": [
    "Задание 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "bc774bb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "top5 = authors_price.nlargest(5, 'price')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "917d40a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author_id</th>\n",
       "      <th>author_name</th>\n",
       "      <th>book_title</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>Чехов</td>\n",
       "      <td>Толстый и тонкий</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Отцы и дети</td>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>Чехов</td>\n",
       "      <td>Дама с собачкой</td>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3</td>\n",
       "      <td>Островский</td>\n",
       "      <td>Гроза</td>\n",
       "      <td>370</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Дворянское гнездо</td>\n",
       "      <td>350</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   author_id author_name         book_title  price\n",
       "3          2       Чехов   Толстый и тонкий    500\n",
       "0          1    Тургенев        Отцы и дети    450\n",
       "4          2       Чехов    Дама с собачкой    450\n",
       "5          3  Островский              Гроза    370\n",
       "2          1    Тургенев  Дворянское гнездо    350"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f7de10b",
   "metadata": {},
   "source": [
    "Задание 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "f41a462f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "authors_stat1 = authors_price.groupby('author_name').agg({'price' : 'min'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "b4c0df44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>author_name</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Островский</th>\n",
       "      <td>290</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Тургенев</th>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Чехов</th>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             price\n",
       "author_name       \n",
       "Островский     290\n",
       "Тургенев       300\n",
       "Чехов          450"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "authors_stat1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "7bf983a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "authors_stat2 = authors_price.groupby('author_name').agg({'price' : 'min'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "bc3ff59f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>author_name</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Островский</th>\n",
       "      <td>290</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Тургенев</th>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Чехов</th>\n",
       "      <td>450</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             price\n",
       "author_name       \n",
       "Островский     290\n",
       "Тургенев       300\n",
       "Чехов          450"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "authors_stat2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "9ff7277d",
   "metadata": {},
   "outputs": [],
   "source": [
    "authors_stat3 = authors_price.groupby('author_name').agg({'price' : 'mean'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "1d26edc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>author_name</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Островский</th>\n",
       "      <td>330.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Тургенев</th>\n",
       "      <td>366.666667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Чехов</th>\n",
       "      <td>475.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  price\n",
       "author_name            \n",
       "Островский   330.000000\n",
       "Тургенев     366.666667\n",
       "Чехов        475.000000"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "authors_stat3"
   ]
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
