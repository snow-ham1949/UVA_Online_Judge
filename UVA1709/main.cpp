#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 1000000 + 6;

double max_price[MAXN], price[MAXN];

int main() {

    int p, a, b, c, d, n;
    while (scanf("%d %d %d %d %d %d", &p, &a, &b, &c, &d, &n) != EOF)
    {
        for (int i = 1; i <= n; ++i)
        {
            price[i] = (double)p * (sin(a * i + b) + cos(c * i + d) + 2);
            max_price[i] = max(max_price[i - 1], price[i]);
        }

        double ans = 0.0;
        for (int i = 1; i <= n; ++i)
        {
            ans = max(max_price[i - 1] - price[i], ans);
        }

        printf("%.6f\n", ans);
    }

    return 0;
}
