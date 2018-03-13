//Code Working Properly:
//Check for Robustness!
#include<queue>
#include<vector>
#include<stdlib.h>
#include<iostream>

#define STRAIGHT_COST 10
#define DIAGONAL_COST 14

using namespace std;

class Points{
	//Private Definitions:a
	private:
		int xPos;
		int yPos;
		int fValue;
		int gValue;
		int hValue;
		Points* parentPtr;
		bool orphan;

		public:
		//Constructor and Destructor
		Points(){
			this->orphan = 0;
		}
		//~Points();

		// Methods
		//-----------------Getter Functions--------------------------------
		int get_xPos() 	const{ return this->xPos;   }
		int get_yPos() 	const{ return this->yPos;   }
		int get_fVal() 	const{ return this->fValue; }
		int get_gVal() 	const{ return this->gValue; }
		int get_hVal() 	const{ return this->hValue; }

		bool get_orphan() const{return this->orphan;}

		Points* get_parent()const{
			return parentPtr;
		}
		//--------------------------------------------------------------------


		//--------------Setter Functions---------------------------------------
		void set_orphan(bool orp){
			this->orphan = orp;
		}
		void set_parent(Points* newparent){
			this->parentPtr = newparent;
		}

		void set_xPos(int x){
			this->xPos = x;
		}

		void set_yPos(int y){
			this->yPos = y;
		}

		void set_hVal (int hValue){
			this->hValue = hValue;
		}

		void set_gVal (int move_cost){
			this->gValue = move_cost;
		}

		void set_fVal(){
			this->fValue = this->gValue + this->hValue;
		}
		//------------------------------------------------------------

		friend bool operator > (const Points& lhs, const Points& rhs);
};

//-------------For Priority Queue-----------------------------------
bool operator > (const Points& lhs, const Points& rhs){
	return lhs.get_fVal() > rhs.get_fVal();
}
//------------------------------------------------------------------



void a_star(int *map, int size, int *start, int *finish){
// Initialise Priority Queue
priority_queue<Points, vector<Points>, greater<vector<Points>::value_type> >open_set;
// Map is a one-d array [row*size + col]// Initialise object point in a 2d array
	Points point[size*size];
	Points node;
	bool success = 0;

	int i;
	int j;
	int min_i;
	int min_j;
	int max_i;
	int max_j;
	int current_gcost;
	int current_x = start[0];
	int current_y = start[1];
	point[current_y*size + current_x].set_parent(NULL);
	point[current_y*size + current_x].set_xPos(current_x);
	point[current_y*size + current_x].set_yPos(current_y);
	point[current_y*size + current_x].set_gVal(0);
	point[current_y*size + current_x].set_hVal(( abs(finish[0]-current_x) + abs(finish[1]-current_y))*10 );
	point[current_y*size + current_x].set_fVal();
	point[current_y*size + current_x].set_orphan(1);

	open_set.push(point[current_y*size + current_x]);


//----------------------THE BIG LOOP--------------------------------------------
//------------------------------------------------------------------------------
	while(!success && !open_set.empty()){
		node = open_set.top();
		open_set.pop();
		current_gcost = node.get_gVal();
		min_i = (node.get_xPos()==0)?0 : -1;
		min_j = (node.get_yPos()==0)?0 : -1;
		max_i = (node.get_xPos()==(size-1))?0: 1;
		max_j = (node.get_yPos()==(size-1))?0: 1;

//----------------------------LOOP TERMINATING CONDITIONS-----------------------
		if(node.get_hVal() <= DIAGONAL_COST){
			point[finish[0] + size*finish[1]].set_parent(&point[node.get_yPos()*size + node.get_xPos()]);
			success = 1;
			cout << "Successful!" << endl;
			break;
		}
//----------------------------analyze neighbors---------------------------------
		for(j = min_j; j <= max_j; j++){
			for(i = min_i; i <= max_i; i++){

				if(!(map[(node.get_yPos() + j)*size + (node.get_xPos() + i)] ==1) || (i==0&&j==0)){


					if (point[(node.get_yPos() + j)*size + node.get_xPos() + i].get_orphan() == 1){

						int new_gcost = point[node.get_yPos()*size + node.get_xPos()].get_gVal() + ((abs(i)==abs(j))? DIAGONAL_COST : STRAIGHT_COST);
						if (new_gcost < point[(node.get_yPos() + j)*size + node.get_xPos() + i].get_gVal())
							{
							point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_gVal(new_gcost);
							point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_parent(&point[node.get_yPos()*size + node.get_xPos()]);
							point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_fVal();
							}
					}
					else{

						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_orphan(1);
						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_hVal( (abs(node.get_xPos() + i - finish[0]) + abs(node.get_yPos() + j - finish[1])) * STRAIGHT_COST);
						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_gVal( (current_gcost) + ( (abs(i)==abs(j))? DIAGONAL_COST : STRAIGHT_COST) );
						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_fVal();
						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_parent(&point[node.get_yPos()*size + node.get_xPos()]);
						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_xPos(node.get_xPos() + i);
						point[(node.get_yPos() + j)*size + node.get_xPos() + i].set_yPos(node.get_yPos() + j);
						open_set.push(point[(node.get_yPos() + j)*size + node.get_xPos() + i]);
					}
				}
			}
		}
//------------------------------------------------------------------------------

	}
//------------------------End of Big LOOP---------------------------------------
//------------------------------------------------------------------------------
	vector<Points*> path;
	Points* foo;
	foo = &node;
	if(success){
		path.push_back(foo);
		while(foo->get_parent() != NULL ){
			path.push_back(foo->get_parent());
			foo = foo->get_parent();
		}
		cout <<endl<<"Total Path Length:"<<path.size() << endl ;
		for(vector<Points*>::iterator it = path.begin(); it != path.end() ; it++){
			foo = *it ;
			map[(foo->get_xPos()) + (foo->get_yPos())*size] = 2;
		}
		for(int i = 0 ; i < size ; i++){
			for (int j = 0; j< size ; j++){
				cout << map[i * size + j];
			}
			cout << endl;
		}
	}
	if(!success){
		cout << endl << "No Path Found!" << endl;
	}
}

int main(){
	int map[] = {
		0,0,0,1,0,0,0,0,0,0,
		0,1,0,1,0,0,0,0,1,0,
		0,1,0,1,0,0,0,0,1,0,
		0,1,0,1,0,0,0,0,1,0,
		0,1,0,1,0,0,1,0,1,0,
		0,1,0,1,0,0,1,0,1,0,
		0,1,0,1,0,0,1,0,1,0,
		0,1,0,1,0,0,1,0,0,0,
		0,1,0,1,0,0,1,0,0,0,
		0,1,0,0,0,0,1,0,0,0
	};
	int size = 10;
	int start[] = {0,0};
	int finish[] = {9,9};

	a_star(map, size, start,finish);
	return 0;
}
