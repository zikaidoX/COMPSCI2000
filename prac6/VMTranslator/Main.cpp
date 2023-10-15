#include <string>
#include <vector>
#include <regex>
#include <iostream>
#include <fstream>
#include <sstream>

#include "VMTranslator.h"

using namespace std;

/** A quick-and-dirty parser */ 
int main(int argc, char** argv){

    if(argc > 1){

        fstream file;
        file.open(argv[1],ios::in);
        if (file.is_open()){   
            VMTranslator vmt;
            string line;
            while(getline(file, line)){
                regex endl_re("\\r*\\n+");
                regex space_re("\\s+");
                line = regex_replace(line, endl_re, "");
                line = regex_replace(line, space_re, " ");
                vector <string> tokens;
                stringstream ss(line);
                string token;
                // Tokenize
                while(getline(ss, token, ' ')){
                    tokens.push_back(token);
                }
                if(tokens.size()==1){
                    if(tokens[0]=="add"){
                        cout << vmt.vm_add() << endl;
                    } else if(tokens[0]=="sub"){
                        cout << vmt.vm_sub() << endl;
                    } else if(tokens[0]=="neg"){
                        cout << vmt.vm_neg() << endl;
                    } else if(tokens[0]=="eq"){
                        cout << vmt.vm_eq() << endl;
                    } else if(tokens[0]=="gt"){
                        cout << vmt.vm_gt() << endl;
                    } else if(tokens[0]=="lt"){
                        cout << vmt.vm_lt() << endl;
                    } else if(tokens[0]=="and"){
                        cout << vmt.vm_and() << endl;
                    } else if(tokens[0]=="or"){
                        cout << vmt.vm_or() << endl;
                    } else if(tokens[0]=="not"){
                        cout << vmt.vm_not() << endl;
                    } else if(tokens[0]=="return"){
                        cout << vmt.vm_return() << endl;
                    }
                } else if(tokens.size()==2){
                    if(tokens[0]=="label"){
                        cout << vmt.vm_label(tokens[1]) << endl;
                    } else if(tokens[0]=="goto"){
                        cout << vmt.vm_goto(tokens[1]) << endl;
                    } else if(tokens[0]=="if-goto"){
                        cout << vmt.vm_if(tokens[1]) << endl;
                    }
                } else if(tokens.size()==3){
                    int t2;
                    try {
                        t2 = stoi(tokens[2]);
                    } catch (const invalid_argument& ia) {
                        cerr << "Unable to parse int." << tokens[2] << endl;
                        break;
                    }
                    if(tokens[0]=="push"){
                        cout << vmt.vm_push(tokens[1],t2) << endl;
                    } else if(tokens[0]=="pop"){
                        cout << vmt.vm_pop(tokens[1],t2) << endl;
                    } else if(tokens[0]=="function"){
                        cout << vmt.vm_function(tokens[1],t2) << endl;
                    } else if(tokens[0]=="call"){
                        cout << vmt.vm_call(tokens[1],t2) << endl;
                    }
                }
            }
            file.close();
        }

    }
} 
