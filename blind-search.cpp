#include <bits/stdc++.h>

struct node
{
    string tag="";
    list<node *> neighbors;
};
struct AGB{
    private: 
    bool firstInAmplitude=false;
    bool firstInDepth=false;
    public: 
    AGB(string algorithm)
    {
        if(algorithm=="FIA"){
            firstInAmplitude=true;
        }else if(algorithm=="FID"){
            firstInDepth=true;
        }
    }
    List<node *> opened_nodes;
    List<node *> closed_nodes;
    node* next(List<node *>& nodes_list){
        
    }
}


int main(){
    return 0;
}