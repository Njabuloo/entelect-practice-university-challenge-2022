# Entelect University Cup 2022

This is my solution for the 2022 Entelect University cup Practrice round, which is a decoding challenge.

## Problem description

Develop a solution to decode a map and identify hidden numbers

There are four different terrain types and each terrain has a different elevation range.

In this repo, there are three different maps to decode.

More information can be found in the `Specification.pdf`

## How to run

```
git clone git@github.com:Njabuloo/entelect-practice-university-challenge-2022.git
cd entelect-practice-university-challenge-2022
pip3 install -r requirements.txt
python main.py
```

## Solution

1. Create a map by populating a numpy array using the terrains given.
2.  If the number assign to the array square is within the range of the mountain, assing the square to 1, otherwise 0.
3.  create an image from the map array.
4.  use an ocr library (easyocr) to extract the hidden number in the image.

## Results 

### Map1 ( small : 15*30)
![MAP 1](https://github.com/Njabuloo/entelect-practice-university-challenge-2022/blob/main/map_1.png)
> "91"

### Map2 ( Medium : 30*60 )
![MAP 2](https://github.com/Njabuloo/entelect-practice-university-challenge-2022/blob/main/map_2.png)
>"07"

### Map3 ( Large : 60 * 120)
![MAP 3](https://github.com/Njabuloo/entelect-practice-university-challenge-2022/blob/main/map_3.png)
>"74"

## Conclusion

The solution works for the small and medium maps. 

It does not work for the large map, this might be caused by using different fonts when training the easyocr detection model and also the noise in the image.
