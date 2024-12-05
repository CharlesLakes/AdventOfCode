#include <bits/stdc++.h>
#define forn(i,i0,n) for(int i = i0; i < n; i++)
typedef long long ll;
using namespace std;
map<ll,vector<ll>> g;
int main(){
    ll m; cin >> m;
    while(m--){
        ll a,b; cin >> a >> b;
        g[a].push_back(b);
    }
    ll n; cin >> n;
    ll ans = 0;
    while(n--){
        ll l; cin >> l;
        vector<ll> nums(l);
        for(ll &a: nums) cin >> a;
        bool flag = true;
        set<ll> vis;
        forn(i,0,l){
            for(ll a: g[nums[i]]) flag = flag && !vis.count(a);
            vis.insert(nums[i]);
        }
        if(flag){
            ans += nums[(l-1)/2];
        }
    }
    cout << ans << endl;


    return 9;
}