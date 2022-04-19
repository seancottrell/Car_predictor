{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3456c9e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "82c5dbca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        HipHop\n",
       "1        HipHop\n",
       "2        HipHop\n",
       "3          Jazz\n",
       "4          Jazz\n",
       "5          Jazz\n",
       "6     Classical\n",
       "7     Classical\n",
       "8     Classical\n",
       "9         Dance\n",
       "10        Dance\n",
       "11        Dance\n",
       "12     Acoustic\n",
       "13     Acoustic\n",
       "14     Acoustic\n",
       "15    Classical\n",
       "16    Classical\n",
       "17    Classical\n",
       "Name: genre, dtype: object"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('music.csv')\n",
    "X= df.drop(columns=['genre'])\n",
    "y = df['genre']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "30535203",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['HipHop', 'Dance'], dtype=object)"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "\n",
    "\n",
    "model= DecisionTreeClassifier()\n",
    "model.fit(X,y)\n",
    "predictions= model.predict([[21,1],[22,0]])\n",
    "predictions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "39a7c006",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)#the amount of data I am feeding to the model\n",
    "model.fit(X_train,y_train)\n",
    "predictions= model.predict(X_test)\n",
    "\n",
    "score=accuracy_score(y_test,predictions)\n",
    "\n",
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "a1a3c7c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['HipHop'], dtype=object)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "\n",
    "df = pd.read_csv('music.csv')\n",
    "X= df.drop(columns=['genre'])\n",
    "y = df['genre']\n",
    "\n",
    "\n",
    "model= DecisionTreeClassifier()\n",
    "model.fit(X,y)\n",
    "\n",
    "predictions= model.predict([[21,1]])\n",
    "predictions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "69eae9c7",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'joblib' from 'sklearn.externals' (/Volumes/T7/opt/anaconda3/lib/python3.9/site-packages/sklearn/externals/__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/jx/4n05wnhd3sqdnldjg7p3yv340000gn/T/ipykernel_33368/3995099256.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtree\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDecisionTreeClassifier\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexternals\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'music.csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mImportError\u001b[0m: cannot import name 'joblib' from 'sklearn.externals' (/Volumes/T7/opt/anaconda3/lib/python3.9/site-packages/sklearn/externals/__init__.py)"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.externals import joblib\n",
    "\n",
    "df = pd.read_csv('music.csv')\n",
    "X = df.drop(columns=['genre'])\n",
    "y = df['genre']\n",
    "\n",
    "\n",
    "model= DecisionTreeClassifier()\n",
    "model.fit(X,y)\n",
    "\n",
    "joblib.dump(model,\"music-recommender.joblib\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ec6f37f6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'joblib' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/jx/4n05wnhd3sqdnldjg7p3yv340000gn/T/ipykernel_33368/3642447799.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmodel\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmodel\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"music-recommender.joblib\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'joblib' is not defined"
     ]
    }
   ],
   "source": [
    "model= joblib.load(model,\"music-recommender.joblib\")\n",
    "model.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "2ded31a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn import tree\n",
    "\n",
    "df = pd.read_csv('music.csv')\n",
    "X = df.drop(columns=['genre'])\n",
    "y = df['genre']\n",
    "\n",
    "\n",
    "model= DecisionTreeClassifier()\n",
    "model.fit(X,y)\n",
    "\n",
    "tree.export_graphviz(model, out_file='music-recommender.dot',\n",
    "                    feature_names=['age', 'gender'],\n",
    "                     class_names=sorted(y.unique()),\n",
    "                     label='all',\n",
    "                     rounded=True,\n",
    "                     filled=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "37bf2522",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Text(200.88000000000002, 181.2, 'X[0] <= 30.5\\ngini = 0.778\\nsamples = 18\\nvalue = [3, 6, 3, 3, 3]'),\n",
       " Text(133.92000000000002, 108.72, 'X[1] <= 0.5\\ngini = 0.75\\nsamples = 12\\nvalue = [3, 0, 3, 3, 3]'),\n",
       " Text(66.96000000000001, 36.23999999999998, 'gini = 0.5\\nsamples = 6\\nvalue = [3, 0, 3, 0, 0]'),\n",
       " Text(200.88000000000002, 36.23999999999998, 'gini = 0.5\\nsamples = 6\\nvalue = [0, 0, 0, 3, 3]'),\n",
       " Text(267.84000000000003, 108.72, 'gini = 0.0\\nsamples = 6\\nvalue = [0, 6, 0, 0, 0]')]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.tree import plot_tree\n",
    "\n",
    "\n",
    "\n",
    "tree_clf2= DecisionTreeClassifier(max_depth=2, max_leaf_nodes=3,\n",
    "                                  min_samples_split=2,random_state=42)\n",
    "tree_clf2.fit(X,y)\n",
    "\n",
    "plot_tree(tree_clf2,filled= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aac56595",
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
