using System.Collections.Generic;
using System;
using System.Runtime.CompilerServices;

namespace MyGradientBorder
{
    public class GradientBorder
    {
        //private List<List<int>> _originalGreyImage;
        private List<List<(int, int)>> _gradientVectorMatrix;
        private List<List<double>> _gradientVectorLengths;
        private List<List<int>> _gradientVectorAngles;
        private double _maxLength;

        public List<List<int>> BorderMatrix
        {
            get;
            private set;
        }

        private List<List<int>> _sobelOperatorX = new()
        {
            new List<int>() { -1, 0, 1 },
            new List<int>() { -2, 0, 2 },
            new List<int>() { -1, 0, 1 }
        };
        private List<List<int>> _sobelOperatorY = new()
        {
            new List<int>() { -1, -2, -1 },
            new List<int>() { 0, 0, 0 },
            new List<int>() { 1, 2, 1 }
        };

        public GradientBorder(List<List<int>> originalImage)
        {
            GetGradientComponents(originalImage);
        }

        private int GetAngle(int intx, int y)
        {
            double x = intx;
            if (intx == 0)
                x = 0.01;

            double tan = y / x;

            if ((x > 0 && y < 0 && tan < -2.414) || (x < 0 && y < 0 && tan > 2.414))
            {
                return 0;
            }
            else if (x > 0 && y < 0 && tan < -0.414)
            {
                return 1;
            }
            else if ((x > 0 && y < 0 && tan > -0.414) || (x > 0 && y > 0 && tan < 0.414))
            {
                return 2;
            }
            else if (x > 0 && y > 0 && tan < 2.414)
            {
                return 3;
            }
            else if ((x > 0 && y > 0 && tan > 2.414) || (x < 0 && y > 0 && tan < -2.414))
            {
                return 4;
            }
            else if (x < 0 && y > 0 && tan < -0.414)
            {
                return 5;
            }
            else if ((x < 0 && y > 0 && tan > -0.414) || (x < 0 && y < 0 && tan < 0.414))
            {
                return 6;
            }
            else if (x < 0 && y < 0 && tan < 2.414)
            {
                return 7;
            }
            else if (x > 0)
            {
                return 2;
            }
            else if (x < 0)
            {
                return 6;
            }
            else
            {
                throw new Exception();
            }

        }

        private void GetGradientComponents(List<List<int>> originalImage)
        {
            int convSize2 = _sobelOperatorX.Count() / 2;
            _gradientVectorMatrix = new();
            _gradientVectorAngles = new();
            _gradientVectorLengths = new();
            _maxLength = -100000;

            for (int i = convSize2; i < originalImage.Count() - convSize2; i++)
            {
                _gradientVectorMatrix.Add(new List<(int, int)>());
                _gradientVectorLengths.Add(new List<double>());
                _gradientVectorAngles.Add(new List<int>());

                for (int j = convSize2; j < originalImage[i].Count() - convSize2; j++)
                {
                    (int, int) value = (0, 0);
                    int ii = 0;
                    for (int k = i - convSize2; k < i + convSize2 + 1; k++)
                    {
                        int jj = 0;
                        for (int c = j - convSize2; c < j + convSize2 + 1; c++)
                        {
                            value.Item1 += originalImage[k][c] * _sobelOperatorX[ii][jj];
                            value.Item2 += originalImage[k][c] * _sobelOperatorY[ii][jj];
                            jj++;
                        }
                        ii++;
                    }

                    _gradientVectorMatrix[i - 1].Add(value);
                    double length = Math.Sqrt(Math.Pow(value.Item1, 2) + Math.Pow(value.Item2, 2));
                    if (length > _maxLength)
                    {
                        _maxLength = length;
                    }
                    _gradientVectorLengths[i - 1].Add(length);
                    _gradientVectorAngles[i - 1].Add(GetAngle(value.Item1, value.Item2));

                }
            }
        }


        private void DestroyNonMax()
        {
            BorderMatrix = new List<List<int>>();
            for (int i = 0; i < _gradientVectorAngles.Count; i++)
            {
                BorderMatrix.Add(new List<int>());
                for (int j = 0; j < _gradientVectorAngles[i].Count; j++)
                {
                    int ang = _gradientVectorAngles[i][j];
                    if (i == 0 || j == 0 || i == _gradientVectorAngles.Count() - 1 || j == _gradientVectorAngles[i].Count() - 1)
                    {
                        BorderMatrix[i].Add(0);
                    }
                    else if (ang == 0 || ang == 4)
                    {
                        if (_gradientVectorLengths[i][j] > _gradientVectorLengths[i - 1][j] && _gradientVectorLengths[i][j] > _gradientVectorLengths[i + 1][j])
                        {
                            BorderMatrix[i].Add(255);
                        }
                        else
                        {
                            BorderMatrix[i].Add(0);
                        }
                    }
                    else if (ang == 2 || ang == 6)
                    {
                        if (_gradientVectorLengths[i][j] > _gradientVectorLengths[i][j - 1] && _gradientVectorLengths[i][j] > _gradientVectorLengths[i][j + 1])
                        {
                            BorderMatrix[i].Add(255);
                        }
                        else
                        {
                            BorderMatrix[i].Add(0);
                        }
                    }
                    else if (ang == 3 || ang == 7)
                    {
                        if (_gradientVectorLengths[i][j] > _gradientVectorLengths[i + 1][j + 1] && _gradientVectorLengths[i][j] > _gradientVectorLengths[i - 1][j - 1])
                        {
                            BorderMatrix[i].Add(255);
                        }
                        else
                        {
                            BorderMatrix[i].Add(0);
                        }
                    }
                    else if (ang == 1 || ang == 5)
                    {
                        if (_gradientVectorLengths[i][j] > _gradientVectorLengths[i - 1][j + 1] && _gradientVectorLengths[i][j] > _gradientVectorLengths[i + 1][j - 1])
                        {
                            BorderMatrix[i].Add(255);
                        }
                        else
                        {
                            BorderMatrix[i].Add(0);
                        }
                    }

                }
            }

        }

        private void DoubleFiltering(int low, int high)
        {
            int low_bord = Convert.ToInt32(_maxLength / low);
            int high_bord = Convert.ToInt32(_maxLength / high);

            for (int i = 0; i < BorderMatrix.Count; i++)
            {
                for (int j = 0; j < BorderMatrix[i].Count; j++)
                {
                    if (BorderMatrix[i][j] == 255 && _gradientVectorLengths[i][j] >= high_bord)
                    {
                        BorderMatrix[i][j] = 255;
                    }
                    else if (BorderMatrix[i][j] == 255 && _gradientVectorLengths[i][j] <= low_bord)
                    {
                        BorderMatrix[i][j] = 0;
                    }
                    else if (BorderMatrix[i][j] == 255)
                    {
                        BorderMatrix[i][j] = 100;
                    }
                }
            }

            for (int i = 1; i < BorderMatrix.Count - 1; i++)
            {
                for (int j = 1; j < BorderMatrix[i].Count - 1; j++)
                {
                    if (BorderMatrix[i][j] == 100)
                    {
                        bool b = false;
                        for (int k = i - 1; k < i + 2; k++)
                        {
                            for (int c = j - 1; c < j + 2; c++)
                            {
                                if (BorderMatrix[k][c] == 255)
                                {
                                    BorderMatrix[i][j] = 255;
                                    b = true;
                                    break;
                                }
                            }
                        }
                        if (b == false)
                        {
                            BorderMatrix[i][j] = 0;
                        }
                    }
                }
            }
        }

        public List<List<int>> GetBorder(int low, int high, bool filter = false)
        {
            DestroyNonMax();
            if (filter)
            {
                DoubleFiltering(low, high);
            }
            return BorderMatrix;
        }


    }
}