#include <chrono>
#include <thread>
using std::cout;
using std::endl;
using std::chrono::duration_cast;
using std::chrono::milliseconds;
using std::chrono::nanoseconds;
using std::chrono::seconds;
using std::chrono::system_clock;
void cysleep(long long int x){
    std::this_thread::sleep_for(milliseconds(x));
}
void cysleep_force(long long int x_nano){
    auto start_time =  duration_cast<nanoseconds>(system_clock::now().time_since_epoch()).count();
    while (duration_cast<nanoseconds>(system_clock::now().time_since_epoch()).count() - start_time <= x_nano){
        bool nigger = true;
    }

}