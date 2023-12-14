#include <bits/stdc++.h>

using namespace std;
typedef __int128 ll;

struct GCD_type { ll x, y, d; };
GCD_type ex_GCD(ll a, ll b){
  if (b == 0) return {1, 0, a};
  GCD_type pom = ex_GCD(b, a % b);
  return {pom.y, pom.x - a / b * pom.y, pom.d};
}
ll crt(vector<ll> a, vector<ll> m){
  int n = a.size();
  for (int i = 0; i < n; i ++){
    a[i] %= m[i];
    a[i] = a[i] < 0 ? a[i] + m[i] : a[i];
  }
  ll ans = a[0];
  ll M = m[0];
  for (int i = 1; i < n; i ++){
    auto pom = ex_GCD(M, m[i]);
    ll x1 = pom.x;
    ll d = pom.d;
    if ((a[i] - ans) % d != 0)
      return -1;
    ans = ans + x1 * (a[i] - ans) / d % (m[i] / d) * M;
    M = M * m[i] / d;
    ans %= M;
    ans = ans < 0 ? ans + M : ans;
    M = M / __gcd(M, m[i]) * m[i];
  }
  return ans;
}


ll read128_t() {
  string S; cin >> S;
  if (S == "0") return 0;
  __int128_t res = 0;
  for (int i = S[0] == '-' ? 1 : 0; i < (int)S.size(); i++)
    res = res * 10 + S[i] - '0';
  if (S[0] == '-') res = -res;
  return res;
}
string parse128_t(ll x) {
  if (x == 0) return "0";
  bool neg = false;
  if (x < 0) neg = true, x = -x;
  string res;
  while (x) res.push_back(x % 10 + '0'), x /= 10;
  if (neg) res.push_back('-');
  reverse(begin(res), end(res));
  return res;
}

int main(){
    vector<ll> as = {10959,15455,17703,1967,0,12083};
    vector<ll> ms = {16579,18827,19951,12083,22199,17141};
    cout << parse128_t(crt(as,ms)) << endl;
    

    return 0;
}
