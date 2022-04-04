#include <stdio.h>
#define Max_size 6
#define Max_stack_size 100
int stack_end = -1;
int init_x = -1;
int init_y = -1;
void push(); // to push the next step in the stack
void find_mouse();  // initial mouse row & col
void print_maze();	// print maze every move to see the movement
void print_stack(); // print stack for see what (row,col) is in stack
typedef struct x_y_location {
	short x;
	short y;
} x_y_location;  // an structure about row,col

x_y_location x_y_stack[Max_stack_size];  // a stack which is an array for row and col information ( data structure = x_y_location )
x_y_location pop();

char maze[Max_size][Max_size] = {			// the maze  1:wall,0:empty space,e:mouse,x:exit
		{'1', '1', '1', '1', '1', '1'},
		{'e', '0', '1', '0', '0', '1'},
		{'1', '0', '0', '0', '1', '1'},
		{'1', '0', '1', '0', '1', '1'},
		{'1', '0', '1', '0', '0', 'x'},
		{'1', '1', '1', '1', '1', '1'},
};

int dx[] = { 0,1,0,-1 };   //  a array for search east,west,north,south
int dy[] = { 1,0,-1,0 };

void main() {
	printf("  START!\n\n");
	find_mouse();			// initial mouse row col location
	if (init_x == -1 || init_y == -1) {
		printf("can't find mice!");
		return;
	}
	push(init_x, init_y); //push init_row and init_col of the mouse initial row,col
	print_maze();
	printf("\n");
	int cnt = 1;
	while (stack_end >= 0) {	// stack_end means the rear of the array if it's -1 it means its empty
		x_y_location info = pop(); // pop row,col value from stack
		short x = info.x;
		short y = info.y;
		int added = 0;
		for (int dir = 0; dir < 4; dir++) { // search e,w,n,s
			short nx = x + dx[dir];
			short ny = y + dy[dir];
			if (0 <= nx < sizeof(maze) && 0 <= ny < sizeof(maze[0])) {   // if nx and ny in the maze area
				if (maze[nx][ny] == '0') { // if the next step is empty space push nx,ny in the stack and change mice row,col and make the before location to . which means visited.
					push(nx, ny);
					init_x = nx;
					init_y = ny;
					maze[x][y] = '.';
					maze[nx][ny] = 'e';
					printf("--move %d--\n\n", cnt); // display which move is now
					print_maze();
					printf("\n");
					print_stack();
					added = 1;
					cnt += 1;
				}
				else if (maze[nx][ny] == 'x') { // if next step is x print escape and end the program
					maze[x][y] = '.';
					maze[nx][ny] = 'e';
					print_maze();
					printf("¡Ú escape ¡Ú\n\n");
					return;
				}
			}
			if (!(added)) {
				maze[x][y] = '.';
			}
		}
	}

}

void push(short x, short y) {
	x_y_location new_location = { x,y };

	if (stack_end + 1 < Max_stack_size) {
		x_y_stack[stack_end + 1] = new_location;
		stack_end = stack_end + 1;
	}
	else {
		printf("stack is full.");
	}
}

x_y_location pop() {									// returns the stack rear row,col value
	x_y_location temp = x_y_stack[stack_end];
	stack_end--;

	return temp;
}

void find_mouse() {
	for (int i = 0; i < Max_size; i++) {
		for (int j = 0; j < Max_size; j++) {
			if (maze[i][j] == 'e') {
				init_x = i;
				init_y = j;
				return;
			}
		}
	}
}

void print_maze() {

	for (int i = 0; i < Max_size; i++) {
		printf("  ");
		for (int j = 0; j < Max_size; j++) {
			printf("%c", maze[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void print_stack() {   // show's the value in the stack
	printf("  |STACK|\n");
	for (int i = stack_end; i >= 0; i--) {
		printf("  |%d , %d|\n", x_y_stack[i].x, x_y_stack[i].y);
	}
	printf("-----------\n\n");
}