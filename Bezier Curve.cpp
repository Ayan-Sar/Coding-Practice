#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>

#define MAX_POINTS 10

typedef struct {
    int x, y;
} 
point_t;
/* Function to calculate the binomial coefficient */
int binomial(int n, int k) {
    int res = 1;
    if (k > n - k) {
        k = n - k;
    }
    for (int i = 0; i < k; i++) {
        res *= (n - i);
        res /= (i + 1);
    }
    return res;
}

/* Function to calculate the value of the Bezier curve at parameter t */
point_t bezier(point_t *points, int n, double t) {
    point_t res = {0, 0};
    for (int i = 0; i < n; i++) {
        int b = binomial(n - 1, i);
        double u = pow(1 - t, n - 1 - i) * pow(t, i);
        res.x += b * u * points[i].x;
        res.y += b * u * points[i].y;
    }
    return res;
}

/* Function to draw the Bezier curve */
void draw_bezier(point_t *points, int n) {
    for (double t = 0; t <= 1; t += 0.01) {
        point_t p = bezier(points, n, t);
        putpixel(p.x, p.y, WHITE);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    point_t points[MAX_POINTS];
    int n = 0;

    /* Read in control points from user input */
    printf("Enter control points (x y), one per line. End with a blank line.\n");
    char line[80];
    while (fgets(line, sizeof(line), stdin)) {
        if (line[0] == '\n') {
            break;
        }
        sscanf(line, "%d %d", &points[n].x, &points[n].y);
        n++;
        if (n == MAX_POINTS) {
            break;
        }
    }

    draw_bezier(points, n);

    getch();
    closegraph();
    return 0;
}