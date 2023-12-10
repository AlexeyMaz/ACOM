using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System;

namespace GaussianBlur
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            Bitmap originalImage = new Bitmap("C:\\Users\\AlmaZ\\PycharmProjects\\acom\\resources\\2.jpg");

            List<List<int>> bwImage = new List<List<int>>();

            for (int y = 0; y < originalImage.Height; y++)
            {
                List<int> row = new List<int>();
                for (int x = 0; x < originalImage.Width; x++)
                {
                    Color pixel = originalImage.GetPixel(x, y);
                    int brightness = (int)(pixel.R * 0.3 + pixel.G * 0.59 + pixel.B * 0.11);
                    row.Add(brightness);
                    originalImage.SetPixel(x, y, Color.FromArgb(255, brightness, brightness, brightness));
                }
                bwImage.Add(row);
            }
            pictureBox1.Image = originalImage;

            var list = MyGauss.GaussianBlur(bwImage, 21, 3);

            if (list == bwImage)
            {
                throw new Exception();
            }

            Bitmap blured = new Bitmap(originalImage);
            for (int y = 0; y < blured.Height; y++)
            {
                for (int x = 0; x < blured.Width; x++)
                {
                    blured.SetPixel(x, y, Color.FromArgb(255, list[y][x], list[y][x], list[y][x]));
                }
            }
            pictureBox2.Image = blured;
        }
    }
}