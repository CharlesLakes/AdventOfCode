#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>
#define forn(i,i0,n) for(int i = int(i0); i < int(n); ++i)
#define USM ios_base::sync_with_stdio(false),cin.tie(NULL)
#define double long double
#define endl '\n'

using namespace std;

typedef int ll;

set<char> rright = {'-','J','7'};
set<char> lleft = {'-','L','F'};
set<char> top = {'|','7','F'};
set<char> bottom = {'|','L','J'};

vector<set<char>> ifs = {
    {'S','|','L','J'},
    {'S','|','7','F'},
    {'S','-','L','F'},
    {'S','-','J','7'}
};

int main() {
    USM;
    vector<string> matriz;
    string in;
    while(cin >> in)
        matriz.push_back(in);

    ll n = matriz.size();
    ll m = matriz[0].size();
    vector<vector<ll>> dist(n,vector<ll>(m,INT_MAX));
    ll x,y;
    forn(i,0,n)
        forn(j,0,m)
            if(matriz[i][j]=='S'){
                x = i; y = j;
            }

    stack<pair<ll,ll>> q;
    q.push({x,y});
    dist[x][y] = 0;
    vector<vector<bool>> vis(n,vector<bool>(m,false));
    ll cnt = 0;
    vector<pair<ll,ll>> points;
    while(!q.empty()){
        auto p = q.top();
        q.pop();
        if(vis[p.first][p.second]) continue;
        vis[p.first][p.second] = true;
        
        cnt++;
        points.push_back(p);
        
        if(ifs[1].count(matriz[p.first][p.second]) && p.first + 1 >= 0 && p.first + 1 < n &&
            bottom.count(matriz[p.first + 1][p.second]) && 
            dist[p.first][p.second] + 1 < dist[p.first + 1][p.second]) {q.push({p.first + 1,p.second}); dist[p.first + 1][p.second] = dist[p.first][p.second] + 1;}
        if(ifs[0].count(matriz[p.first][p.second]) && p.first - 1 >= 0 && p.first - 1 < n &&
            top.count(matriz[p.first - 1][p.second]) && 
            dist[p.first][p.second] + 1 < dist[p.first - 1][p.second]) {q.push({p.first - 1,p.second}); dist[p.first - 1][p.second] = dist[p.first][p.second] + 1;}
        if(ifs[2].count(matriz[p.first][p.second]) && p.second + 1 >= 0 && p.second + 1 < m &&
            rright.count(matriz[p.first][p.second + 1]) && 
            dist[p.first][p.second] + 1 < dist[p.first][p.second + 1]) {q.push({p.first,p.second + 1}); dist[p.first][p.second + 1] = dist[p.first][p.second] + 1;}
        if(ifs[3].count(matriz[p.first][p.second]) && p.second - 1 >= 0 && p.second - 1 < m &&
            lleft.count(matriz[p.first][p.second - 1]) && 
            dist[p.first][p.second] + 1 < dist[p.first][p.second - 1]) {q.push({p.first,p.second - 1}); dist[p.first][p.second - 1] = dist[p.first][p.second] + 1;}
    }
    points.push_back({x,y});
    ll ans = 0;
    forn(i,0,int(points.size()) - 1){
        ans += points[i].first*points[i + 1].second;
        ans -= points[i].second*points[i + 1].first;
    }   
    
    ans = abs(ans);
    ans = ans - cnt + 2;
    ans /= 2;
    cout << ans << endl;


    return 0;
}