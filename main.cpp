/*
 * esasharahi@gmail.com
 * Make and Run: g++ -I/usr/include/python2.7 main.cpp -lpython2.7 -o main && ./main
 * Consider the SODE dy_i/dt = f_i; i = 1, 2. 
 */

#include "/usr/include/python2.7/Python.h" /* Should be first include. Find it by locate Python.h in your system*/
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

const double h = 0.2;
const double t_0 = 0.0;
const double y_1_0 = 0;
const double y_2_0 = 1;
const double iter = 2000;

double f_1(double t, double y_1, double y_2){
	return y_2;
	}

	double f_2(double t, double y_1, double y_2){
	return 0 ;
	}


int main (){

	double t = t_0;
	double y_1 = y_1_0;
	double y_2 = y_2_0;


	ofstream storefile_1;
	storefile_1.open ("points1.txt");

	ofstream storefile_2;
	storefile_2.open ("points2.txt");

	ofstream storefile_3d;
	storefile_3d.open ("points3d.txt");


	for (int i = 0; i <= iter; i++){
			double k_1_1 = f_1(t, y_1, y_2);
			double k_1_2 = f_2(t, y_1, y_2);

			double k_2_1 = f_1(t + (h / 2), y_1 + (h / 2) * k_1_1, y_2 + (h / 2) * k_1_2);
			double k_2_2 = f_2(t + (h / 2), y_1 + (h / 2) * k_1_1, y_2 + (h / 2) * k_1_2);

			double k_3_1 = f_1(t + (h / 2), y_1 + (h / 2) * k_2_1, y_2 + (h / 2) * k_2_2);
			double k_3_2 = f_2(t + (h / 2), y_1 + (h / 2) * k_2_1, y_2 + (h / 2) * k_2_2);
			
			double k_4_1 = f_1(t + h, y_1 + h * k_3_1, y_2 + h * k_3_2);
			double k_4_2 = f_2(t + h, y_1 + h * k_3_1, y_2 + h * k_3_2);

			cout << "i: " << i << endl;
			cout << t << " " << y_1 << endl;
			storefile_1 <<  t << " " << y_1 << endl;
			cout << t << " " << y_2 << endl;
			storefile_2 <<  t << " " << y_2 << endl;
			storefile_3d <<  t << " " << y_1 << " " << y_2 << endl;
			cout << endl;

			y_1 = y_1 + (h / 6) * (k_1_1 + 2 * k_2_1 + 2 * k_3_1 + k_4_1);
			y_2 = y_2 + (h / 6) * (k_1_2 + 2 * k_2_2 + 2 * k_3_2 + k_4_2);
			t = t + h;
			}

	storefile_1.close();
	storefile_2.close();
	storefile_3d.close();

	char filename[] = "ploter.py";
		FILE* fp;
		Py_Initialize();
		fp = fopen(filename, "r");
		PyRun_SimpleFile(fp, filename);
		Py_Finalize();
}
